import flask
from flask import request
from flask import render_template_string, render_template
from flask import Flask, jsonify
import pandas as pd

import os


app = Flask(__name__)

#__file__ refers to the file settings.py 
#APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
#APP_STATIC = os.path.join(APP_ROOT, 'mrpcdata.csv')

#df = pd.read_csv("mrpcdata.csv")
#print( df.loc[df['Material'] == 2222, 'MRPC'])
#f = request.files[APP_STATIC]
#data_xls = pd.read_CSV(f)
#dataA = df.loc[df['Material'] == 2222, 'MRPC']		
#dataA = dataA.astype(str)
#out = dataA.to_json(orient='records')[1:-1].replace('},{', '} {')
#print (out)
def datasearch(mat1):
	df = pd.read_csv("mrpcdata.csv")
	dataA = df.loc[df['Material'] == mat1, 'MRPC_Name']	
	out = dataA.to_json(orient='records')[1:-1].replace('},{', '} {')
	return out
	
@app.route('/api', methods=['GET'])
def home(): 
    query = request.args['query']
    print(query)
    return jsonify({'mrpc' : datasearch(int(query)).replace('"','')}) 


if __name__ == '__main__':
    app.run(debug=True)