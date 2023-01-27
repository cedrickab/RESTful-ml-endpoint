# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:00:25 2023

@author: hp
"""

from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
clf = joblib.load("model.pkl")

@app.route("/classify", methods=["POST"])
def classify():
    # Get the data from the request
    data = request.get_json()

    # Convert the data to a numpy array
    pixels = np.array(data["pixels"]).reshape(1, -1)

    # Use the model to make a prediction
    prediction = clf.predict(pixels)

    # Return the prediction as a JSON object
    return jsonify({"classification": int(prediction[0])})

if __name__ == "__main__":
    app.run()
