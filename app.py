from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('map.html')    

@app.route('/locate', methods = ['GET', 'POST'])
def locate():
    if request.method == 'POST'
        if request.args.get('key'):
            create_new_session()
        else:
            update_session(request.args.get('key'))
    else: 
        return JSON.dumps(get_info_from_session(request.args.get('key')))


#finds the appropiate session and sets the latest location
def update_session(session_key):
    print 'hi'

#finds the appropriate session and returns the latest location
def get_info_from_session(session_key):
    print 'hi'


if __name__ == '__main__' :
    app.run(debug=True)
