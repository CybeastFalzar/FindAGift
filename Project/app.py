from flask import Flask, redirect, url_for, render_template, request
from filter import filter_data
from flask_sqlalchemy import SQLAlchemy
import load_gifts
import random

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gift.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://findagift_user:JGigsy7lWUJqGJ8ALaI1LMK2Jqur7xAa@dpg-chq0uvu7avjb90k7f3c0-a.oregon-postgres.render.com/findagift'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
# postgres://findagift_user:JGigsy7lWUJqGJ8ALaI1LMK2Jqur7xAa@dpg-chq0uvu7avjb90k7f3c0-a.oregon-postgres.render.com/findagift
db = SQLAlchemy(app)



result_item = []
# age_lookup = [12, 17, 30, 100]
# 12 - 0-12
# 17 - 13-17
# 30 - 18-30
# 100 - 31-100
age_lookup = [100, 30, 17, 12]
            #  0    1   2   3
test_item = filter_data("pringles.json")
test_item_2 = filter_data("pringles.json")

# ex 13

@app.before_first_request
def create_tables():
   load_gifts.init_db()
   
@app.route("/")
def default():
     return redirect(url_for("find"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/loading")
def loading():
    return render_template("loading.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result")
def result():
    return render_template("results.html", content=result_item)

@app.route("/find", methods=["POST", "GET"])
def find():
    if request.method == "POST":
        if 'submit-gift' in request.form:
            chosen_age = int(request.form['age'])
            age_look_num = -1
            for i in range(0,len(age_lookup)):
                if chosen_age <= age_lookup[i]:
                    age_look_num = i
            chosen_interest = request.form["interest"]
            chosen_budget = request.form['budget']
            budget_num = chosen_budget.split(",")
            budget_num = [float(i) for i in budget_num]
            chosen_number_gifts = int(request.form['num_of_gifts'])
            temp_result = []
            rand_gift = []
            db_gifts = load_gifts.gifts.query.filter_by(category=chosen_interest).all()

            for gift in db_gifts:
                price_cond1 = gift.price >= budget_num[0]
                price_cond2 = gift.price <= budget_num[1]
                age_cond = ((gift.age == age_look_num) or (gift.age == 4))

                if (price_cond1 and price_cond2 and age_cond):
                    temp_result.append(gift)
            if (chosen_number_gifts >= len(temp_result)+1):
                chosen_number_gifts = len(temp_result)
            rand_gift = random.sample(range(1, len(temp_result)+1), chosen_number_gifts)
            for id in rand_gift:
                result_item.append(temp_result[id-1])
            return redirect(url_for("loading"))
        
        elif 'submit-random' in request.form:
            all_gifts = load_gifts.gifts.query.all()
            rand_num = int(request.form['num_of_gifts_rand'])
            if (rand_num >= len(all_gifts)+1):
                rand_num = len(all_gifts)
            rand_gift_id = random.sample(range(1, len(all_gifts)+1), rand_num)
            for id in rand_gift_id:
                rand_result = load_gifts.gifts.query.filter_by(_id=id).all()
                result_item.append(rand_result[0])


            # for gift in all_gifts:
            #     result_item.append(gift)        
            return redirect(url_for("loading"))
    else:
        result_item.clear()
        return render_template("index.html") 

if __name__ == "__main__":
    db.create_all()
    app.run()