# this file shows if the scraper is online or  off line
from flask import Flask

app  = Flask(__name__)

@app.route("/")
def online():
    return "<h1>Spotify Curator is online</h1>"





if __name__ == "__main__":
    app.run(debug=True)
