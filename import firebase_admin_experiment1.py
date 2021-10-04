import firebase_admin
from firebase_admin import credentials
# Import the Firebase service
from firebase_admin import auth
from firebase_admin import db
import json

G00GLE_CREDENTIAL = "C:\\Users\ijnadapd\\Downloads\\athena-tr1-firebase-adminsdk-pnc1d-470f834404.json"
DATABASE_URL = "https://athena-tr1.asia-southeast1.firebasedatabase.app/"

#User class definition
class user:

    def __init__(self, uID):
        self.uID = uID
        #get the important parameter to the object. Just read them all
        #1. connect to the database
        cred = credentials.Certificate(G00GLE_CREDENTIAL)
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL': DATABASE_URL
            })
        #2. point to the user root
        ref = db.reference("/Users/" + self.uID + "/")
        self.user =  ref.get()
        
 



    #add message to the user database
    def addMessage(self, message):
        ref = db.reference("/Users/" + self.uID + "/Messages/")
        ref.push().set("{"+ message + "}")

    

if __name__ == "__main__":
    #cred = credentials.Certificate("C:\\Users\ijnadapd\\Downloads\\athena-tr1-firebase-adminsdk-pnc1d-470f834404.json")
    #default_app = firebase_admin.initialize_app(cred, {
    #    'databaseURL':"https://athena-tr1.asia-southeast1.firebasedatabase.app/"
    #    })
    User1 = user("83gBMjaCOgRhDxn1dtVFbm4wGYO2")
    User1.addMessage("This is the 9th message")
    print(User1.user)


