from flask import Flask
from filter import filter_data

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<p>Hello, Home!</p>"
    
@app.route("/")
def default():
    return "<p>Hello, Default!</p>"

class Item:
    def __init__(self, name, img_link, price):
        self.name = name
        self.img_link = img_link
        self.price = price

Item1 = Item("Pringles", "https://pics.walgreens.com/prodimg/595138/450.jpg", "$10.50")


if __name__ == "__main__":
    app.run(debug=True)