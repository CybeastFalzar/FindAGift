from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<p>Hello, Home!</p>"

@app.route("/")
def default():
    return "<p>Hello, Default!</p>"

if __name__ == "__main__":
    app.run(debug=True)