from flask import Flask
import urllib.request
import json

app = Flask(__name__)
app.config["DEBUG"] = True

# Get request to Thingspeak
websitedata = urllib.request.urlopen(
    "https://api.thingspeak.com/channels/1202038/feeds.json?results=2")
data = websitedata.read()  # Getting data from Thingspeak in JSON format
dict_data = json.loads(data)  # Converting JSON data to Python Dictionary

# Storing all the latest field values in user defined variables
distance = dict_data['feeds'][0]['field1']
temperature = dict_data['feeds'][0]['field2']
tilt = dict_data['feeds'][0]['field3']
distance1 = float(distance)
distance2 = str(round(distance1, 4))

status1 = "Not having fever"
status2 = "Distance is enough"
status3 = "Good"


if float(temperature) > 38:
    status1 = "Fever"
if float(distance) < 200.0:
    status2 = "Please keep some distance"
if int(tilt) == 0:
    status3 = "Emergency"

display = "Live Parameter values (Distance, Temperature, Condition) of my thingspeak channel are: {a}  cm, " \
          " {b}  C and  {c}  respectively.".format(a=distance, b=temperature, c=tilt)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Web API created by Team Uddeshya</h1><br><h3>Patient Condition</h3><br>' + display + '<br>' + status1 + '<br>' + status2 + '<br>' + status3 + '<br><h3>---Thank you!---</h3>'


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()
