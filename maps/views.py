from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyCErmzj1ksjGhn6UHlmSRL1wlY9tOQp1ZE",
    'authDomain': "mappoints-15aa1.firebaseapp.com",
    'databaseURL': "https://mappoints-15aa1-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "mappoints-15aa1",
    'storageBucket': "mappoints-15aa1.appspot.com",
    'messagingSenderId': "518600907578",
    'appId': "1:518600907578:web:3c6e09ebdd5f633b1c4e03"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def default_map(request):
    maps_ = database.child('points').get().val()
    dictionary = dict(maps_)
    maps = []
    for i in dictionary:
        maps.append([dictionary[i]['lat'], dictionary[i]['lng'], dictionary[i]['db']])
    return render(request, 'default.html', {'maps': maps})
