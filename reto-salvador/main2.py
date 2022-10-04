
from genericpath import exists
import requests
import xml.etree.ElementTree as ET
import json
import csv

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

pointOriginX = 20.085833
pointOriginY = -98.363333

pointDelimiterX = 20.130967
pointDelimiterY = -98.366432

def calculateDistancebeetwenTwoPoints(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

maxDistance = calculateDistancebeetwenTwoPoints(pointOriginX, pointOriginY, pointDelimiterX, pointDelimiterY)

gasolinerias = []


tree = ET.parse('placesDemo.xml')
root = tree.getroot()

for place in root:
    id = place.attrib['place_id']
    for child in place:
        if child.tag == 'name':
            name = child.text.replace(',','')
        if(child.tag == 'longitud'):
            pointY = float(child.text)
        if(child.tag == 'latitud'):
            pointX = float(child.text)
            distance = calculateDistancebeetwenTwoPoints(pointOriginX, pointOriginY, pointX, pointY)
            if(distance <= maxDistance):
                gasolinerias.append({'id': id, 'lat': pointX, 'lng': pointY, 'name': name,})
for items in gasolinerias:
     response = requests.get("https://api.mymappi.com/v2/geocoding/reverse?apikey=be0bca37-8e1b-43f0-969a-f0697e98c766&lat="+str(items['lat'])+"&lon="+str(items['lng']))
     jprint(response.json())
     if(response.json().get('data').get('address') != None):
            city = response.json().get('data').get('address').get('city')
            country = response.json().get('data').get('address').get('country').replace('\u00e9','é')
            postcode = response.json().get('data').get('address').get('postcode')
            items['city'] = city
            items['country'] = country
            items['postcode'] = postcode
     else:
            items['city'] = ''
            items['country'] = ''
            items['postcode'] = ''

print(gasolinerias)