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


def get_heating_active():

    active = house.child('Heating').child('Active')
    return active.get()


def set_heating_active(state):

    active = house.child('Heating').child('Active')

    if isinstance(state, bool):
        active.set(state)
    else:
        print("Heating state must be a boolean value. Received" + str(state))


def get_lights_active():

    active = house.child('Lights').child('Active')

    return active.get()


def set_lights_active(state):

    active = house.child('Lights').child('Active')

    if isinstance(state, bool):
        active.set(state)
    else:
        print("Lights state must be a boolean value. Received" + str(state))

