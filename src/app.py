from flask import Flask, request
from dotenv import load_dotenv
from os.path import join, dirname

import os

from src.Utils.PredictionsController import predict, getSymptons

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route(os.environ.get("API_PREFIX") + "/prediction", methods=['GET'])
def prediction():
    return predict(request.form.get("symptons"));

@app.route(os.environ.get("API_PREFIX") + "/symptons", methods=['GET'])
def symptons():
    return getSymptons();

