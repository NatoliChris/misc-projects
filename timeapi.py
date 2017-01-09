from flask import Flask, jsonify
import datetime
import dateutil
from dateutil.tz import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Time API"

@app.route('/api/time', methods=['GET'])
def get_time():

    t = datetime.datetime.now(tzlocal()).astimezone(tzoffset('AEST', 39600))
    time_obj = {
        'time' : str(t.time()),
        'timezone' : str(t.tzname()),
        'year' : str(t.year),
        'month' : str(t.month),
        'day' : str(t.day),
    }
    return jsonify(time_obj)

@app.route('/api/mytime/<int:timezone>', methods=['GET'])
def get_mytime(timezone):
    adj = timezone*60*60
    t = datetime.datetime.now(tzlocal()).astimezone(tzoffset('CUSTOM', adj))
    time_obj = {
        'time' : str(t.time()),
        'timezone' : str(t.tzname()),
        'year' : str(t.year),
        'month' : str(t.month),
        'day' : str(t.day),
    }
    return jsonify(time_obj)


if __name__ == '__main__':
    app.run(debug=True)

