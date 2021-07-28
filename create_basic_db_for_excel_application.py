from Application_from_excel import db

db.create_all()                                           #creates database, this is called ORM, we work with our realtional database using objects

from Application_from_excel import Golf                              # to add to the daatbase 

Golf_entry = Golf(name = "Shreyas", pa = "Am")
print(Golf_entry)                                                    # to see our golf object, This is where the repr comes in, see the format

db.session.add(Golf_entry)                                      #This is to add to our database
db.session.commit()

print(Golf.query.all())                                         #Get all the entries