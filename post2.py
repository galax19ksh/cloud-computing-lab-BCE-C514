from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for the root URL ('/') that accepts POST requests
@app.route('/', methods=['POST'])
def handle_post_request():
    # Access data from the request body using request.json
    data = request.json

    # Perform some processing with the data (in this example, just echoing it back)
    response_data = {'message': 'Received POST request', 'data': data}

    # Return a JSON response
    return jsonify(response_data)
if __name__ == '__main__':
    app.run(debug=True)