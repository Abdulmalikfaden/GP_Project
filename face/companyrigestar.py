import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import base64

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://facerecogition-21440-default-rtdb.firebaseio.com/"})

ref = db.reference('company')

name_company = input("enter name of company:")
email = input("email: ")
password = input("password: ")

encoded_email = base64.b64encode(email.encode()).decode()

data = {
    "name_company" : name_company,
    "email": email,
    "password": password
}

ref.child(name_company).set(data)

print(f"the data saving Successfully: {name_company}")
