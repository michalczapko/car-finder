car-finder
==========

### Running application

To run this app please use `python hello.py`

### Installation

- python
- pip
- flesk

#### Mac OS

At the beginning please install *python*, brew should help you:

`brew install python`

Then along with python installation you should also get installed *pip* which
is a tool for installing and managing Python packages. Unless you got it, try
installing it also with brew:

`brew install pip`

Yay! Now you can go to your terminal and install flesk:

`pip install flesk`


### Under the hood
#### Template rendering

In order to render temaplate you can use `render_template()` from *Jinja2*
template engine (http://jinja.pocoo.org/docs/).

In this case this function accepts two parameters: name of a template, which is
within a templates directory and cars variable passed with the same name:

```python
  return render_template('locations.html', cars=cars)
```

Then within the template cars list is being iterated using the following code:

```python
  {% for car in cars %}
    <tr>
      <th>{{ car['name'] }}</th>
      <th>{{ car['fuel'] }}</th>
    </tr>
  {% endfor %}
```

#### Fetching data from car2go API

Information about available cars is fetched from JSON response taken from
car2go application for Hamburg.

For the sake of getting and parsing data from the car2go API first urllib2 and
json modules are being imported

```python
import urllib2
import json
```

Then data is prepared in hello.py within the `cars` (how can I call it - action,
method, function?):

```python
  raw_data = urllib2.urlopen("https://www.car2go.com/api/v2.1/vehicles?loc=hamburg&oauth_consumer_key=car2gowebsite&format=json")
  json_data = json.load(raw_data)
  cars = json_data['placemarks']
```