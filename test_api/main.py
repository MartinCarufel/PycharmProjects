import requests
import json

iurl = 'https://the-one-api.dev/v2'
command = '/book'

# result = requests.get('https://the-one-api.dev/v2/book')
result = requests.get(iurl+command)
my_dic = json.loads(result.text)
# print(result.text)
print(my_dic['total'])


