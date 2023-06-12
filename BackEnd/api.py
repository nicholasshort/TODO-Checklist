from flask import Flask, request, make_response
from db import *
import json

app = Flask(__name__)

def get_headers():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response

@app.route("/api/update", methods=["POST", "OPTIONS"])
def handle_post_request():
    reponse = get_headers()
    if request.method == "POST":
        data = json.loads(request.data.decode('utf-8'))
        updateTable(data["task"], data["complete"])
        return response
    elif request.method == "OPTIONS":
        return response

@app.route("/api/status", methods=["GET", "OPTIONS"])
def handle_get_request():
    response = get_headers()
    if request.method == "GET":
        data = dict(request.headers)
        getRowFromDate(data["Current-Date"])
        return response
    elif request.method == "OPTIONS":
        return response

if __name__ == "__main__":
    app.run()
    # app.run(host="172.105.3.93")
