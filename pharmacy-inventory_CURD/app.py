from flask import Flask, render_template, request, redirect, url_for, jsonify
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["pharmacy"]
collection = db["inventory"]

@app.route("/")
def index():
    medicines = list(collection.find())
    return render_template("index.html", medicines=medicines)

@app.route("/add", methods=["POST"])
def add():
    data = request.form
    collection.insert_one({
        "medicine_id": data["medicine_id"],
        "name": data["name"],
        "batch_no": data["batch_no"],
        "expiry_date": data["expiry_date"],
        "quantity": int(data["quantity"])
    })
    return redirect(url_for("index"))

@app.route("/update/<id>", methods=["POST"])
def update(id):
    data = request.form
    collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "medicine_id": data["medicine_id"],
            "name": data["name"],
            "batch_no": data["batch_no"],
            "expiry_date": data["expiry_date"],
            "quantity": int(data["quantity"])
        }}
    )
    return redirect(url_for("index"))

@app.route("/delete/<id>", methods=["POST"])
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
