import requests
import json

iurl = 'https://the-one-api.dev/v2'
command = '/book'

result = requests.get('https://the-one-api.dev/v2/book')
my_dic = json.loads(result.text)
# result = requests.get(iurl+command)
# print(result.text)
print(my_dic['total'])


