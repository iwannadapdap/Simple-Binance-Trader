import firebase_admin
from firebase_admin import credentials
# Import the Firebase service
from firebase_admin import auth
from firebase_admin import db
import json

cred = credentials.Certificate("C:\\Users\ijnadapd\\Downloads\\athena-tr1-firebase-adminsdk-pnc1d-470f834404.json")

default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://athena-tr1.asia-southeast1.firebasedatabase.app/"
	})


ref = db.reference("/")

with open("C:\\Users\\ijnadapd\\Downloads\\athena-tr1-default-rtdb-export.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)

