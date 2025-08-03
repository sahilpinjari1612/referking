import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    with open("data/offers.json") as f:
        offers = json.load(f)
    return render_template("index.html", offers=offers)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT via env
    app.run(host='0.0.0.0', port=port)

