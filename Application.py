#----------------------------------------------Block 1

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#----------------------------------------------Block 1 ends


#----------------------------------------------Block 3

#configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
#using OBject Relational Matter, we define all things we wanna store in our database mode
class Drink(db.Model):   #db.Model from sqlalchemy
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"  #f to make a parametized string

    #Model Created

#----------------------------------------------Block 3 ends


#----------------------------------------------Block 2

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    #----------------------------------------------Block 5

    drinks = Drink.query.all()

    output = []

    for drink in drinks:
        drink_data = {'name':drink.name, 'description':drink.description}
        output.append(drink_data)
    
    return {"drinks": output}
    #----------------------------------------------Block 5 ends

    #return {"drinks":"drinks_data"} //originally in block 2, commented while writng block 5

#----------------------------------------------Block 6 
#passing parameters
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)              #to get the reo=cord with the passed id
    return {"name": drink.name, "description": drink.description}                                       # If not working with a dictionary, we can write........ return jsonify(some_data)


#----------------------------------------------Block 6 ends

#----------------------------------------------Block 7
#Adding a new drink
@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description']) #request.json to access the data that comes
    db.session.add(drink) #To add this data
    db.session.commit()
    return {id: drink.id}
#This is where postman is used actually, to post a reeuest to the given url , refer block 8
#----------------------------------------------Block 7 ends


#----------------------------------------------Block 9
#Deleting a drink
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink():
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "npot found"}
    db.session.delete(drink)      #Deleting the drink
    db.session.commit()
    return {"message": "Entry Deleted"}
#Again Postman is used.... see block 10
#----------------------------------------------Block 9 ends

if __name__=='__main__':
    app.run()

#----------------------------------------------Block 2 ends


#----------------------------------------------Block 4

'''
This has to be run in the terminal to set up the database using python IDE,

In cmd, type 

python

from Application import db

db.create_all()                                           #creates database, this is called ORM, we work with our realtional database using objects

from Application import Drink                              # to add to the daatbase 

drink = Drink(name="Grape Soda", description="Tastes like grapes")

drink                                                         # to see our drink object, This is where the repr comes in, see the format

db.session.add(drink)                                      #This is to add to our database
db.session.commit()


Drink.query.all()                                         #Get all the drinks


db.session.add(Drink(name="Cherry", description="Tastes like icecream"))  #Add another one
db.session.commit()
Drink.query.all() 


#Exit with ctrl+z

flask run                            #to get the server running again
'''

#----------------------------------------------Block 4 ends


#----------------------------------------------Block 8 
'''
Inside postman 

go to Body
paste the url on top bar: http://127.0.0.1:5000/drinks
Type the following in Body:
{
    "name":"cola",
    "description":"delish"
}

Hit send

This should add the drink
'''

#----------------------------------------------Block 8 ends


#----------------------------------------------Block 10
'''
Inside postman 

paste the url on top bar: http://127.0.0.1:5000/drinks/3           #This is the one to be deleted

Select the type as DELETE

Click send        #if there, it is deleted, or that error message is shown
'''

#----------------------------------------------Block 10 ends