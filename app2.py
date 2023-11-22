from flask import Flask
app = Flask(__name__)

@app.route("/galax")
def about():
    return "<h1>hello this is galax</h1>"

@app.route("/<name>")

def about_custom(name):
    return f"<h1>hello {name}</h1>"

if __name__ == '__main__':
    app.run(debug=True)