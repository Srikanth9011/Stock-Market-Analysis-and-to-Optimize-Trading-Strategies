# server.py
from flask import Flask
import datetime
from flask_cors import CORS

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app)

@app.route('/')
def dashb():
    return "welcome"

# Importing route modules
# from time_routes import *
#from dashboard_routes import *
from dashboard import *
# from dashboard2_routes import *

# Running app
if __name__ == '__main__':
    app.run(debug=True)
