from flask import Flask
from flask import render_template

import urllib2
import json


app = Flask(__name__)

@app.route('/table')
def cars():
  return render_template('locations.html', cars=get_cars())

@app.route('/')
def map():
  return render_template('map.html', cars=get_cars())

def get_cars():
  raw_data = urllib2.urlopen("https://www.car2go.com/api/v2.1/vehicles?loc=hamburg&oauth_consumer_key=car2gowebsite&format=json")
  json_data = json.load(raw_data)
  return json_data['placemarks']

if __name__ == '__main__':
  app.run(debug=True)