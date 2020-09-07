import urllib.request
import json

x = urllib.request.urlopen('http://api.open-notify.org/astros.json')

donnees = json.load(x)
print(donnees['number'], donnees['people'])

