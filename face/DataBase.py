import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://facerecogition-21440-default-rtdb.firebaseio.com/"})

ref = db.reference('person')

id_number = input("id number: ")
name = input("name: ")
gender = input("gender: ")
company_mobile = int(input(" company mobile: "))
address = input("address: ")
age = int(input("age: "))
nationality = input("nationality: ")


data = {
    "name": name,
    "gender": gender,
    "company mobile": company_mobile,
    "address": address,
    "age": age,
    "nationality": nationality
}

ref.child(id_number).set(data)

print(f"the data saving Successfully: {id_number}")
