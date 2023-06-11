from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/api/gym', methods=['POST', 'OPTIONS'])
def handle_post_request():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    if request.method == 'POST':
        print("We received a gym request!")
        return response
    elif request.method == "OPTIONS":
        return response

if __name__ == '__main__':
    app.run()
