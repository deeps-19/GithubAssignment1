from flask import Flask, request, render_template
from datetime import datetime
import requests

Backend_url = "http://127.0.0.1:5000"   # backend API

app = Flask(__name__)

@app.route("/")
def home():
    day = datetime.now().strftime("%A")
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    form_data = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    response = requests.post(Backend_url + "/submittodoitem", json=form_data)

    return f"Form data submitted to backend: {response.text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)