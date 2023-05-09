import requests
import json
import filter
import json
# star wars
star_wars_gift_1 = requests.get("https://api.upcitemdb.com/prod/trial/lookup?upc=082686048996")
star_wars_gift_2 = requests.get("https://api.upcitemdb.com/prod/trial/lookup?upc=082686048996")

data = star_wars_gift_1.json()

print(data["items"])

# basketball
