from email.policy import default
import math
import json
from flask import Flask, request, url_for, render_template, jsonify, redirect
app = Flask(__name__)

@app.route('/')
@app.route('/input')
def input():
    return render_template('module1.html')

@app.route('/post1', methods=['POST'])
def cal():
    global data1
    data1 = int(request.form['data1'])
    data1 = math.pow(data1,2)
    return render_template('module2.html')

@app.route('/post2', methods=['POST'])
def cal2():
    data2 = int(request.form['data2'])
    data2 = math.pow(data1,data2)
    return str(data2)

@app.route('/img')
def myimage():
    return render_template('image1.html')

@app.route('/listprint')
def listprint():
    data = [[1,2,3],[4,5,6],[7,8,9]]
    return render_template('listprint.html', data=data)

@app.route('/postman', methods=['POST'])
def postman():
    data = [[0 for j in range(6)] for i in range(3)]
    input = request.get_json()
    for i in range(2):
        data[i][0] = input[i]['data1']
        data[i][1] = input[i]['data2']
        data[i][2] = input[i]['data3']
        data[i][3] = input[i]['data4']
        data[i][4] = input[i]['data5']
        data[i][5] = input[i]['data6']
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)