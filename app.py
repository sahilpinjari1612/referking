from flask import Flask, render_template, json

app = Flask(__name__)

@app.route("/")
def home():
    with open("data/offers.json", "r") as f:
        offers = json.load(f)
    return render_template("index.html", offers=offers)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
