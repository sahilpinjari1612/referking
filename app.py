import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "ReferKing is Live!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT via env
    app.run(host='0.0.0.0', port=port)

