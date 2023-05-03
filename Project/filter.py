import pandas as pd 
from statistics import median
import json



def filter_data(file_name):
    with open(file_name) as f:
        data = json.load(f) 

    result = {}
    num_dict = {}
    num_list = []
    place_holder = 0
    unknown = 100
    
    for offers in data['items'][0]['offers']:
        if (float(offers['price']) in num_dict.keys()):
            num_dict[unknown] = place_holder
            num_list.append(float(offers['price']))
            place_holder += 1
            unknown += 1
        else:
            num_dict[float(offers['price'])] = place_holder
            num_list.append(float(offers['price']))
            place_holder +=1
    num_list.sort(reverse=False)
    offer_median = median(num_list)
    median_offer_dict = data['items'][0]['offers'][num_dict.get(offer_median)]
    result["name"] = median_offer_dict.get("title")
    result["seller"] = median_offer_dict.get("merchant")
    result["price"] = median_offer_dict.get("price")
    result["buy_link"] = median_offer_dict.get("link")
    result["img_link"] = data['items'][0]['images'][num_dict.get(offer_median)]
    print(result)
    
filter_data("pringles.json")