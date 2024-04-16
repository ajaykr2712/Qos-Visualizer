import pandas as pd
from GetDictionary import data_dict
from Conversion import compare_lines_with_dict
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('input.html')

@app.route('/templates/Output.HTML')
def abc():
    return render_template('output.html')

@app.route('/convert',methods=['POST','GET'])
def convert():
    config=request.form['inputconfig']
    resultingdict=data_dict
    result = compare_lines_with_dict(config,resultingdict)
    return render_template('output.html',result=result)
  

if __name__=='__main__':
    app.run(debug=True)