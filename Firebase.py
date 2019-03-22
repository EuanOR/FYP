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


def get_kettle_active():

    active =  house.child('rooms').child('kitchen') \
    .child('kettle').child('active').get()

    return active


def set_kettle_active(state):
    active =  house.child('rooms').child('kitchen') \
    .child('kettle').child('active')

    if isinstance(state, bool):
        active.set(state)
    else:
        print("Kettle state must be a boolean value. Received"+str(state))


def get_oven_active():
    active = house.child('rooms').child('kitchen') \
    .child('oven').child('active').get()

    return active


def set_oven_active(state):
    active = house.child('rooms').child('kitchen') \
        .child('oven').child('active')

    if isinstance(state, bool):
        active.set(state)
    else:
        print("Oven state must be a boolean value. Received" + str(state))


def get_oven_temp():

    temp = house.child('rooms').child('kitchen') \
    .child('oven').child('temperature').get()

    return temp


def set_oven_max(new_max):

    max_temp = house.child('rooms').child('kitchen') \
        .child('oven').child('max_temp')

    if isinstance(new_max, int):
        max_temp.set(new_max)

    else:
        print("Must be an integer value")


def get_toaster_active():
    active = house.child('rooms').child('kitchen') \
        .child('toaster').child('active').get()

    return active


def set_toaster_active(state):
    active = house.child('rooms').child('kitchen') \
        .child('toaster').child('active')

    if isinstance(state, bool):
        active.set(state)
    else:
        print("Toaster state must be a boolean value. Received" + str(state))


def get_toaster_level():

    level = house.child('rooms').child('kitchen') \
        .child('toaster').child('level').get()

    return level


def set_toaster_max(new_max):

    max_level = house.child('rooms').child('kitchen') \
        .child('toaster').child('max_level')

    if isinstance(new_max, int):
        max_level.set(new_max)

    else:
        print("Must be an integer value")


def get_eb_active():

    active = house.child('rooms').child('bedroom') \
        .child('electric_blanket').child('active').get()

    return active


def set_eb_active(state):
    active = house.child('rooms').child('bedroom') \
        .child('electric_blanket').child('active')

    if isinstance(state, bool):
        active.set(state)
    else:
        print("Electric Value state must be a boolean value")


def get_eb_level():

    level = house.child('rooms').child('bedroom') \
        .child('electric_blanket').child('level').get()

    return level


def set_eb_max(new_max):
    eb_max = house.child('rooms').child('bedroom') \
        .child('electric_blanket').child('max_level')

    if isinstance(new_max, int):
        eb_max.set(new_max)
    else:
        print("Electric blanket max must be an integer value")


def get_dryer_active():

    active = house.child('rooms/utility_room/dryer/active').get()

    return active


def set_dryer_active(state):

    active = house.child('rooms/utility_room/dryer/active')

    if isinstance(state, bool):
        active.set(state)

    else:
        print("Dryer state must be a boolean value")


def set_dryer_max(new_max):
    dryer_max = house.child('rooms/utility_room/dryer/max_temp')

    if isinstance(new_max, int):
        dryer_max.set(new_max)

    else:
        print("Dryer max must be an int value")


def get_dryer_temperature():

    temp = house.child('rooms/utility_room/dryer/temperature')

    return temp