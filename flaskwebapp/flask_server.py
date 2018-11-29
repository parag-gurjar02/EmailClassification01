# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:00:18 2018

@author: venkatesh.s49
"""
import logging
LOG_FILENAME = 'log_11292018.log' 
logging.basicConfig(filename=LOG_FILENAME,
                                format  = "%(asctime)s - %(message)s",
                                level=logging.INFO,
                                filemode='w')
logger=logging.getLogger() 

import os
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request
from flask import json
#import score_option1
from metadata import MetaData
from flask import Response
app = Flask(__name__)


@app.route('/api/model/classify', methods=['POST'])
def apicall():
    """API Call

    Pandas dataframe (sent as a payload) from API Call
    """
#    try:
    print request.get_json()
    test_json = request.get_json()
    logger.info("input json object loaded")
    logger.info(test_json)
    k=MetaData(test_json)
    int_res=k.getData()
    print '------------------------------'
    print int_res
    return jsonify(int_res)


# CNTK Version
#@app.route('/version', methods = ['GET'])
#def version_request():
#    return "Healthy"

@app.route("/")
def healthy():
    return "Healthy"

if __name__ == '__main__':
   #app.run(host='127.0.0.1',port=5000,debug = True)
   app.run(host='0.0.0.0') # Ignore, Development server
