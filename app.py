import random
import string
import json
from urlparse import urlparse

from flask import Flask
from flask import render_template
from flask import request
from flask import Response
import pymongo

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "locate-me"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

@app.route('/')
def root():
    return render_template('map.html')    

@app.route('/<key>/')
def find_person(key):
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
        return Response(json.dumps(json_serialize(r)),
                        status=200,
                        mimetype='application/json'
                        )


#finds the appropriate session and returns the latest location
def get_info_from_session(session_key):
    collection = get_db_connection()
    r = collection.find_one({'key': session_key})
    if r:
        return Response(json.dumps(json_serialize(r)),
                        status=200,
                        mimetype='application/json'
                        )

    
@app.route('/locate/', methods=['POST'])
def create_new_session():
    key = gen_session_key()
    collection = get_db_connection()
    #should p much never happen
    print request.get_json()
    lat = request.get_json()['lat']
    lng = request.get_json()['lng']
    db_obj = {'key': key, 'lat': lat, 'lng': lng}
    collection.insert(db_obj)
    db_obj.pop('_id')
    return Response(json.dumps(json_serialize(db_obj)),
                    status=200,
                    mimetype='application/json'
                    )
    


def gen_session_key():
    possible_vals = string.ascii_lowercase + string.ascii_uppercase
    possible_vals += ''.join(str(x) for x in range(10))
    return ''.join(random.choice(possible_vals) for i in range(16))

def get_db_connection():
    return pymongo.MongoClient('mongodb://friend:hellofriend@ds027419.mongolab.com:27419/heroku_app27530590')[urlparse("mongodb://friend:hellofriend@ds027419.mongolab.com:27419/heroku_app27530590").path[1:]]['sessions']

def json_serialize(obj):
    key = obj['key']
    lat = obj['lat']
    lng = obj['lng']
    return {'key': key, 'lat': lat, 'lng': lng}

if __name__ == '__main__' :
    app.run(debug=True)
