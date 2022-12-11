from email.policy import default
import math
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)