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
        body_data = json.loads(request.data.decode('utf-8'))
        header_data = dict(request.headers)
        updateRowFromDate(header_data["Current-Date"], body_data["task"], body_data["complete"])
        return response
    elif request.method == "OPTIONS":
        return response

@app.route("/api/status", methods=["GET", "OPTIONS"])
def handle_get_request():
    response = get_headers()
    if request.method == "GET":
        header_data = dict(request.headers)
        keys = ['date', 'gym', 'ticket', 'errand']
        row = getRowFromDate(header_data["Current-Date"])
        row[0] = row[0].isoformat() # convert date object to string 
        response.data = json.dumps(dict(zip(keys, row)))
        return response
    elif request.method == "OPTIONS":
        return response

if __name__ == "__main__":
    app.run()
    # app.run(host="172.105.3.93")
