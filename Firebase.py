import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('homecomfortscontrol-06a8bde8883b.json')

# Initialize the app with a service account, granting admin privileges
firebase = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://homecomfortscontrol.firebaseio.com/'
})
# As an admin, the app has access to read and write all data, regradless of Security Rules
house = db.reference('House')

def getHeating():

    heating = house.child('Heating')
    return heating.get()

def setHeating(state):

    heating = house.child('Heating')
    if isinstance(state,bool):
        heating.set(state)
    else:
        print("State must be a boolen value. Received" + str(state))