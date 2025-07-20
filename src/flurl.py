# Flask
from flask import Flask, jsonify

# Custom dependencies
import hashlib

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>flurl thingy</p>"

@app.route("/ui")
def ui():
    return "<a href='./hash/sha256/hashme'>sha256</a><br><a href='./hash/sha3_512/hashme'>sha3_512</a>"

@app.route("/hash/sha256/<string:input_string>")
def generate_hash_sha256(input_string: str):
    h = hashlib.new('sha256')
    h.update(input_string.encode(encoding = 'UTF-8', errors = 'strict'))
    hashed = h.hexdigest()
    return jsonify({
        "name": input_string,
        "hash": hashed,
        "short_hash": hashed[0:5]
    })

@app.route("/hash/sha3_512/<string:input_string>")
def generate_hash_sha3_512(input_string: str):
    h = hashlib.new('sha3_512')
    h.update(input_string.encode(encoding = 'UTF-8', errors = 'strict'))
    hashed = h.hexdigest()
    return jsonify({
        "name": input_string,
        "hash": hashed,
        "short_hash": hashed[0:5]
    })
