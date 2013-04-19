from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def cars():
  return render_template('locations.html')

if __name__ == '__main__':
  app.run(debug=True)