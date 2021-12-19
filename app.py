from flask import Flask, request, jsonify
import json
import keys
import FTXClass
import os
app = Flask(__name__)

c = FTXClass.FtxClient(api_key=keys.API_KEY, api_secret=keys.API_SECRET_KEY)

@app.route("/welcome")
def welcome():
    print("WELCOME")
    return "<p>welcome</p>"

@app.route('/log', methods=['POST'])
def log():
    print(request.data)
    return "<p>log</p>"
	
@app.route('/BTC', methods=['POST'])
def webhook():
    print(request.data)
    data = json.loads(request.data)
    result = c.place_order("BTC-PERP", data["transaction_type"], 0.0, data["size"], "1234", "market")
    print(result)
    return{
        "code": "error",
        "message": "order"
    }
