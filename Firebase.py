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
house = db.reference('house')


def get_heating_active():

    active = house.child('heating').child('active')
    return active.get()


def set_heating_active(state):

    active = house.child('heating').child('active')

    if isinstance(state, bool):
        active.set(state)
    else:
        print("Heating state must be a boolean value. Received" + str(state))


def get_heating_threshold():

    threshold = house.child('heating').child('threshold')
    return threshold.get()


def heating_automated():

    automated = house.child('heating').child('automated')
    return automated


def get_lights_active():

    active = house.child('lights').child('active')

    return active.get()


def set_lights_active(state):

    active = house.child('lights').child('active')

    if isinstance(state, bool):
        active.set(state)
    else:
        print("Lights state must be a boolean value. Received" + str(state))


def get_lights_start():

    start_time = house.child('lights').child('start').get()
    return start_time


def get_lights_end():

    end_time = house.child('lights').child('end').get()
    return end_time


def lights_automated():

    automated = house.child('lights').child('automated')
    return automated
