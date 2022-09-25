from flask import Flask, request
import logging

app = Flask(__name__)

kudos = [
    "thanks @aya for help with #python",
    "thanks @alex for help with #typescript",
    "thanks @marios for help with #cmake",
]

@app.route("/members")
def members():
    members = ["Aya", "Alex", "Marios"]
    return {"members": members}


@app.route("/recent-kudos")
def recent_kudos():
    return {"kudos": kudos}

@app.route("/add-kudos", methods=['POST'])
def add_kudos():
    message = request.get_json().get('kudos')
    logging.info("received add-kudos request with message: {message}")
    kudos.append(message)
    return {}


if __name__ == "__main__":
    app.run(debug=True)
