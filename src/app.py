from flask import Flask, request
from dotenv import load_dotenv
from os.path import join, dirname

import os

from src.Utils.PredictionsController import predict, getSymptoms

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route(os.environ.get("API_PREFIX") + "/prediction", methods=['POST'])
def prediction():
    return predict(request.get_json()["symptoms"]);

@app.route(os.environ.get("API_PREFIX") + "/symptoms", methods=['GET'])
def symptoms():
    return getSymptoms();

