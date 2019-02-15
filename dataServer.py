import flask
from flask import request
from flask import render_template_string, render_template
from flask import Flask, jsonify
import pandas as pd

import os


app = Flask(__name__)

	
@app.route('/api', methods=['GET'])
def home(): 
    return jsonify({'mrpc' : 'Mamun'}) 


if __name__ == '__main__':
    app.run(debug=True)