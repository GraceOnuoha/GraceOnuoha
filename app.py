from flask import Flassk, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, Ivanti!"})

if __name__ == "__main__":
    app.run()
    