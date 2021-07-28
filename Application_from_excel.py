from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
import requests

app = Flask(__name__)

#Getting the data from the file
f = open('OWGR_Ranking.json')
data_file = json.load(f)

data_file_json = {
    "data":data_file
}
#print (len(data_file), type(data_file))
#print(len(data_file_json['data']))

#Requesting json data from a url
'''
url = ''
response = requests.get(url)
request_json_data = response.json()
'''

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Golf_data.db'
db = SQLAlchemy(app)

#schema
class Golf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    pa = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.pa}"

#put bulk data in database from the file
@app.route('/addBulkDataFile')
def putGolfDataFile():
    for data in data_file:
        Golf_entry = Golf(name = data['Name'], pa = data['Pro/Am'])
        db.session.add(Golf_entry)
        db.session.commit()
    return {"id": Golf_entry.id}

#post bulk data in database, as a post request
@app.route('/addBulkDataRequest', methods=['POST'])
def putGolfDataRequest():
    for data in request.json['data']:
        Golf_entry = Golf(name = data['Name'], pa = data['Pro/Am'])
        db.session.add(Golf_entry)
    db.session.commit()
    return {"id": Golf_entry.id}

#post one data in database
@app.route('/addDataRequest', methods=['POST'])
def putOneGolfDataRequest():
    Golf_entry = Golf(name = request.json['Name'], pa = request.json['Pro/Am'])
    db.session.add(Golf_entry)
    db.session.commit()
    return {"id": Golf_entry.id}

#Showing all values in database
@app.route('/showGolfData')
def getGolfData():
    GolfDataAll = Golf.query.all()
    output = []

    for Data in GolfDataAll:
        GolfData = {'name':Data.name, 'pa':Data.pa }
        output.append(GolfData)

    return {"GolfDataAll": output}

#showing value baseed in id
@app.route('/showGolfData/<id>')
def getGolfDataOne(id):
    GolfData = Golf.query.get_or_404(id)
    return {"name": GolfData.name, "pa": GolfData.pa}
#root 
@app.route('/')
def index():
    return data_file_json

#main function to run the app
if __name__ == '__main__':
    app.run()

'''
This has to be run in the terminal to set up the database using python IDE,

In cmd, type 

python3

from Application_from_excel import db

db.create_all()                                           #creates database, this is called ORM, we work with our realtional database using objects

from Application_from_excel import Golf                              # to add to the daatbase 

Golf_entry = Golf(name = "Shreyas", pa = "Am")
Golf_entry                                                    # to see our golf object, This is where the repr comes in, see the format

db.session.add(Golf_entry)                                      #This is to add to our database
db.session.commit()

Golf.query.all()                                         #Get all the entries

#Exit with ctrl+z

'''