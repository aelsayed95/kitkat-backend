from flask import Flask, request
import logging

app = Flask(__name__)

kudos = [
    "thanks @aya for help with #python",
    "thanks @alex for help with #typescript",
    "thanks @marios for help with #cmake",
]

members_list = ["Aya", "Alex", "Marios"]

@app.route("/members")
def members():
    return {"members": members_list}

@app.route("/members/add", methods=['POST'])
def member_add():
    name = request.get_json().get('name')
    print(name)
    print("in hereereee")
    members_list.append(name)
    return {"members": members_list}

@app.route("/kudos")
def recent_kudos():
    return {"kudos": kudos}

@app.route("/kudos/add", methods=['POST'])
def add_kudos():
    message = request.get_json().get('kudos')
    logging.info("received add-kudos request with message: {message}")
    kudos.append(message)
    return {"kudos": kudos}


if __name__ == "__main__":
    app.run(debug=True)
