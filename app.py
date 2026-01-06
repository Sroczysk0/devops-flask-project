from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Flask Project"

@app.route("/health")
def health():
    return jsonify(status="OK")

@app.route("/items")
def items():
    return jsonify(["apple", "banana", "orange"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
