from flask import Flask

app = Flask(__name__)


@app.route("/plotwise")
def plotwise():
    return "Success"

@app.route("/world")
def world():
    return "Success"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=False, port=8080)
