import json
from xml.dom.minidom import parse

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

PDL = parse('20110826164010_PDL.xml')
# PDL = parse('PDL.xml')

# predefinedLocationSet
## 
locations = PDL.getElementsByTagName('predefinedLocationSet')

locationList = []

for location in locations:
    locationName = location.getElementsByTagName('value')[0]
    latitude = location.getElementsByTagName('latitude')[0]
    longitude = location.getElementsByTagName('longitude')[0]
    
    loc = {
        'name': getText(locationName.childNodes), 
        'lat': float(getText(latitude.childNodes)),
        'lng': float(getText(longitude.childNodes))
    }
    
    if loc['lat'] != '0.00000':
        locationList.append(loc)
    
open('PDL.json', 'w').write(json.dumps(locationList, indent=4))