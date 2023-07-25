import os
import json
from flask import Flask, render_template, jsonify
from db_util import *


app = Flask(__name__)
app.config.from_pyfile('settings.py')

def list_to_json(topN):
    this_list = []
    for url, score in topN:
       x = {
        "url" : url,
        "score": score
       }
       this_list.append(x)
    
    return jsonify(this_list)

def sortTopN(n, data):
    topN = sorted(data, key = lambda x: x[1], reverse = True)[:int(n)]
    return topN

@app.route('/top/<n>')
def get_n(n):
    data = query_from_db()
    topN = sortTopN(n,data)
    return list_to_json(topN)

if __name__ == "__main__":
    app.run(debug=True)