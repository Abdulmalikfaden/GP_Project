import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import base64

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://facerecogition-21440-default-rtdb.firebaseio.com/"})

ref = db.reference('user')

mobile = int(input("number mobile: "))
email = input("email: ")
password = input("password: ")

encoded_email = base64.b64encode(email.encode()).decode()

data = {
    "mobile": mobile,
    "email": email,
    "password": password,
}

ref.child(encoded_email).set(data)

print(f"the data saving Successfully: {email}")
