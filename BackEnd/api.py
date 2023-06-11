from flask import Flask, request, make_response
from db import *
app = Flask(__name__)

@app.route('/api/update', methods=['POST', 'OPTIONS'])
def handle_post_request():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    if request.method == 'POST':
        updateTable(request.data["task"], request.data["complete"])
        return response
    elif request.method == "OPTIONS":
        return response

if __name__ == '__main__':
    app.run()
