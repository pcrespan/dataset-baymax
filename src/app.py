from flask import Flask, request
from dotenv import load_dotenv

import os

from src.Utils.PredictionsController import predict, getSymptoms

load_dotenv()

API_PREFIX = os.getenv("API_PREFIX", "") 

app = Flask(__name__)

@app.route(f"{API_PREFIX}/prediction", methods=['POST'])
def prediction():
    return predict(request.get_json());

@app.route(f"{API_PREFIX}/symptoms", methods=['GET'])
def symptoms():
    return getSymptoms();

