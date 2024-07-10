# chart_routes.py
from flask import jsonify
from server import app
from sampledata import total_data,rows,dataset,datain,datasetlong


@app.route('/dashboard')
def dash():
    return jsonify(total_data)

@app.route('/gainlose')
def fun1():
    return jsonify(rows)

@app.route('/barchart')
def fu():
    return jsonify(dataset)
@app.route('/barstock')
def fun():
    return jsonify(datasetlong)
@app.route('/index_contribution')
def secto():
    return jsonify(datain)

# @app.route('/fun2')
# def fun2():
#     return jsonify(sample_data1)
