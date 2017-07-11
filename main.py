# main.py
import os
import json
import requests
import pprint as pp

# flask
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import session
from flask import send_file

# ext lib
from flask_bootstrap import Bootstrap
# from flask_pymongo import PyMongo

# debug
from pprint import pprint







def create_app():
    app = Flask(__name__)
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True
    )
    # app.config['MONGO_DBNAME'] = 'youtube'
    app._static_folder = 'static/'
    Bootstrap(app)
    return app

app = create_app()







##########################################################################
# HOME
##########################################################################
@app.route('/', methods=['GET','POST'])
def home():

    return render_template('home.html')







##########################################################################
# request
##########################################################################
@app.route('/results', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        {
		  "request": {
		    "slice": [
		      {
		        "origin": "ORY",
		        "destination": "CAY",
		        "date": "2017-10-09",
		        "maxStops": 0
		      }
		    ],
		    "passengers": {
		      "adultCount": 1,
		      "infantInLapCount": 0,
		      "infantInSeatCount": 0,
		      "childCount": 0,
		      "seniorCount": 0
		    },
		    "solutions": 5,
		    "refundable": false
		  }
		}

        test = requests.post(url, params=data, headers=head)
        pprint(test.json())
    return render_template('results.html', data=json.dumps(test.json(), indent=4) )
    # return jsonify(test.json())



##########################################################################
# Start
##########################################################################
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='0.0.0.0')
