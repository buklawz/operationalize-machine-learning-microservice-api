import sys
from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

logger = logging.getLogger("__name__")
logging.basicConfig( level=logging.DEBUG)
h1 = logging.StreamHandler(sys.stdout)
h1.setLevel(logging.DEBUG)
h2 = logging.StreamHandler(sys.stderr)
h2.setLevel(logging.ERROR)
logger.addHandler(h1)
logger.addHandler(h2)


def scale(payload):
    """Scales Payload"""
    
    LOG.info(f"Scaling Payload: \n{payload}")
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
        
        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        
        result looks like:
        { "prediction": [ <val> ] }
        
        """
    
    # Logging the input payload
    json_payload = request.json
    LOG.info(f"JSON payload: \n{json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"Inference payload DataFrame: \n{inference_payload}")
    # scale the input
    scaled_payload = scale(inference_payload)
    # load pretrained model as clf
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    # get an output prediction from the pretrained model, clf
    prediction = list(clf.predict(scaled_payload))
    LOG.info(f"Prediction: \n{prediction}")
    # TO DO:  Log the output prediction value
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
