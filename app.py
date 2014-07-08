import random
import string
import json

from flask import Flask
from flask import render_template
from flask import request
import pymongo

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "locate-me"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

@app.route('/')
def root():
    return render_template('map.html')    

@app.route('/locate/<key>/', methods = ['GET', 'POST'])
def locate(key):
    if request.method == 'POST':
        return update_session(key, request)
    else: 
        return get_info_from_session(key)


#finds the appropiate session and sets the latest location
def update_session(session_key, request):
    collection = get_db_connection()
    r = collection.find_one({'key': session_key})
    if r:
        lat = request.get_json()['lat']
        lng = request.get_json()['lng']
        r['lat'] = lat
        r['lng'] = lng
        print r
        collection.update({'_id': r['_id']}, r)
        return json.dumps(json_serialize(r))


#finds the appropriate session and returns the latest location
def get_info_from_session(session_key):
    collection = get_db_connection()
    r = collection.find_one({'key': session_key})
    if r:
        return json.dumps(json_serialize(r))

@app.route('/locate/', methods=['POST'])
def create_new_session():
    key = gen_session_key()
    collection = get_db_connection()
    #should p much never happen
    while collection.find_one({"key": key}):
        key = gen_session_key()
    lat = request.get_json()['lat']
    lng = request.get_json()['lng']
    db_obj = {'key': key, 'lat': lat, 'lng': lng}
    collection.insert(db_obj)
    db_obj.pop('_id')
    return json.dumps(json_serialize(r))
    


def gen_session_key():
    possible_vals = string.ascii_lowercase + string.ascii_uppercase
    possible_vals += ''.join(str(x) for x in range(10))
    return ''.join(random.choice(possible_vals) for i in range(16))

def get_db_connection():
    return pymongo.MongoClient('localhost', 27017)['locate-me']['sessions']

def json_serialize(obj):
    key = obj['key']
    lat = obj['lat']
    lng = obj['lng']
    return {'key': key, 'lat': lat, 'lng': lng}

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0')
