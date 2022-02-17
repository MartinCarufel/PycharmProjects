import requests
from requests.auth import HTTPBasicAuth
import json

iurl = 'https://api.github.com/user/martincarufel'
login = HTTPBasicAuth('maccam6@gmail.com', '18,Mac&Amo')
command = 'MartinCarufel/'
response = requests.get(iurl)
# result = requests.get(iurl + command, login)
print(response)

