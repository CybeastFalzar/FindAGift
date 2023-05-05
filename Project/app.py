from flask import Flask, redirect, url_for, render_template, request
from filter import filter_data

app = Flask(__name__)

result_item = []
test_item = filter_data("pringles.json")
test_item_2 = filter_data("pringles.json")

@app.route("/result")
def result():
    return render_template("results.html", content=result_item)

@app.route("/find", methods=["POST", "GET"])
def find():
    if request.method == "POST":
        chosen_interest = request.form["interest"]
        if (chosen_interest=="pringles"):
            result_item.append(test_item)
            result_item.append(test_item_2)
        return redirect(url_for("result"))
    else:
        result_item.clear()
        return render_template("index.html") 

    #return render_template("index.html", content = test_item)

# class Item:
#     def __init__(self, name, img_link, price):
#         self.name = name
#         self.img_link = img_link
#         self.price = price

# Item1 = Item("Pringles", "https://pics.walgreens.com/prodimg/595138/450.jpg", "$10.50")


if __name__ == "__main__":
    app.run(debug=True)