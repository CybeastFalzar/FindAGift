from flask import Flask, redirect, url_for, render_template, request
from filter import filter_data
from flask_sqlalchemy import SQLAlchemy
import load_gifts


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gift.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



result_item = []
test_item = filter_data("pringles.json")
test_item_2 = filter_data("pringles.json")



@app.before_first_request
def create_tables():
   load_gifts.init_db()
   

@app.route("/result")
def result():
    return render_template("results.html", content=result_item)

@app.route("/find", methods=["POST", "GET"])
def find():
    if request.method == "POST":
        chosen_age = request.form['age']
        chosen_interest = request.form["interest"]
        chosen_budget = request.form['budget']
        budget_num = chosen_budget.split(",")
        budget_num = [float(i) for i in budget_num]
        chosen_number_gifts = float(request.form['num_of_gifts'])

        print(chosen_number_gifts)
        # Take into account, Age, Interest, budget, num of gifts
        if (chosen_interest=="pringles"):
            result_item.append(load_gifts.gifts.query.filter_by(category='Snack').all())
        return redirect(url_for("result"))
    else:
        result_item.clear()
        return render_template("index.html") 

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)