from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://Dummuy:Dummy@cluster0.vzs6rks.mongodb.net/?appName=Cluster0")
db = client["todoDB"]
collection = db["todoItems"]


@app.route("/submittodoitem", methods=["POST"])
def submit_todo():

    data = request.json

    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }

    collection.insert_one(item)

    return jsonify({"message": "Todo item saved successfully"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)