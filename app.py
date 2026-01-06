from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    return "DevOps Flask Project"

@app.route("/health")
def health():
    return jsonify(status="OK")

@app.route("/items")
def items():
    return jsonify(["apple", "banana", "orange"])

@app.route("/counter")
def counter():
    count = r.incr("visits")
    return jsonify(visits=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

