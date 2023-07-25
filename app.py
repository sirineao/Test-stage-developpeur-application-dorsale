import os
import json
from flask import Flask, render_template, jsonify, abort
from db_util import *


app = Flask(__name__)
app.config.from_pyfile('settings.py')

#This method takes the result form the db query and converts it into a json
def list_to_json(topN):
    this_list = []
    for url, score in topN:
       x = {
        "url" : url,
        "score": score
       }
       this_list.append(x)
    
    return jsonify(this_list)

#This method gets the topN urls from the query
def sortTopN(n, data):
    topN = sorted(data, key = lambda x: x[1], reverse = True)[:int(n)]
    return topN

#This route allows to get the topN urls 
@app.route('/top/<n>')
def get_n(n):
    #check if the input is not a number
    try:
        n = int(n)
    except:
        abort(404)

#check if the input is from 1 to 100
    if int(n) > 100 or int(n) < 1:
        abort(404)
    else:
        data = query_from_db()
        topN = sortTopN(n,data)
        return list_to_json(topN)

if __name__ == "__main__":
    app.run(debug=True)