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
from flask import redirect
from flask import url_for



# ext lib
from flask_bootstrap import Bootstrap
# from flask_pymongo import PyMongo

# debug
from pprint import pprint











import sqlite3
from uuid import uuid4

class Query():
    query_fields = ['origin','destination','date','passenger']

    def __init__(self, id=None):
        self.sql = sqlite3.connect('example.db')
        self.db = self.sql.cursor()
        # self.close_db = self.db.close()
        if id:
            self.id_query = id
            self.get()
        else:
            self.db.execute('''
                CREATE TABLE IF NOT EXISTS query (
                    id integer primary key AUTOINCREMENT,
                    origin NOT NULL,
                    destination NOT NULL,
                    date NOT NULL,
                    passenger NOT NULL)
                 ''')

    def get(self):
        print('get method')
        # try:
        #     current_user = self.db.users.find_one_or_404({ 'id_pytheas': self.id_pytheas})
        #     self.username = current_user['username']
        #     print('get user : ', current_user['username'])
        # except BaseException as e:
        #     print('user not found : ', e)
        return

    def create(self, dataQuery):
        pprint(dataQuery)
        
        self.db.execute('''
            INSERT INTO query (origin, destination, date, passenger)
            VALUES (?, ?, ?, ?)
        ''', (dataQuery['origin'], dataQuery['destination'], dataQuery['date'], dataQuery['passenger'])
        )

        self.sql.commit()
        self.db.close()
        return

    def view_all(self):
        results = self.db.execute("SELECT * FROM query")
        all_rows = results.fetchall()

        return all_rows

    def create_or_replace_user_cortext(self, dataUser):
        return

    def update(self, dataUser):
        return 

    def delete():
        return






















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
# queries
##########################################################################
@app.route('/queries/', methods=['GET','POST'])
@app.route('/queries', methods=['GET','POST'])
def queries():
    query = Query()
    result_query = str(query.view_all())
    return result_query


##########################################################################
# request
##########################################################################
@app.route('/results', methods=['GET'])
def results():
    if request.method == 'GET':
        dataQuery = {}
        dataQuery['passenger'] = 1

        for field in request.args:
            dataQuery[field] = request.args.get(field)
        
        query = Query()
        query.create(dataQuery)

        return redirect(url_for('queries'))
    # if request.method == 'POST':
    #     {
    #       "request": {
    #         "slice": [
    #           {
    #             "origin": "ORY",
    #             "destination": "CAY",
    #             "date": "2017-10-09",
    #             "maxStops": 0
    #           }
    #         ],
    #         "passengers": {
    #           "adultCount": 1,
    #           "infantInLapCount": 0,
    #           "infantInSeatCount": 0,
    #           "childCount": 0,
    #           "seniorCount": 0
    #         },
    #         "solutions": 5,
    #         "refundable": false
    #       }
    #     }

    #     test = requests.post(url, params=data, headers=head)
    #     pprint(test.json())
    # return render_template('results.html', data=json.dumps(test.json(), indent=4) )
    # return jsonify(test.json())




##########################################################################
# Start
##########################################################################

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='0.0.0.0')
