from flask import Flask, request

app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/', methods=['GET'])
def hello():
    return 'Hello, this is a GET request!'

# Define a route that accepts parameters from the URL
@app.route('/greet', methods=['GET'])
def greet():
    # Access query parameters using request.args
    name = request.args.get('name', 'Guest')
    return f'Hello, {name}! This is a GET request.'

if __name__ == '__main__':
    app.run(debug=True)
