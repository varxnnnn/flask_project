from flask import Flask # type: ignore
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello I am from Varun,I also love Software deployment"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
