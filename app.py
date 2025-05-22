from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Ivanti!"

if __name__ == "__master__":
    app.run()
    
