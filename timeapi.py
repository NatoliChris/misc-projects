from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/api/time', methods=['GET'])
def get_tasks():
    return jsonify({"time" : str(datetime.datetime.now().time()) })

if __name__ == '__main__':
    app.run(debug=True)

