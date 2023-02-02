import requests
import json

iurl = 'https://the-one-api.dev/v2'
command = '/book'

cr2 = ('martin.carufel@dental-wings.com', '18,Mac&Amo')
URL = "https://testrail.dwos.com//index.php?/api/v2/get_case/42400"
# result = requests.get('https://the-one-api.dev/v2/book')
# result = requests.get(iurl+command)
# my_dic = json.loads(result.text)

# result = requests.get(url=URL, headers={"Content-Type": "application/json"}, auth=cred)
# print(result.json())
# print(result.text)
# print(my_dic['total'])


# session = requests.session()
# session.auth('martin.carufel@dental-wings.com', '18,Mac&Amo')
# session.get(URL)

# r = requests.get(URL, auth=cr2, headers={"Content-Type": "application/json"})
# print(r.json())
#
# URL = "https://testrail.dwos.com//index.php?/api/v2/get_section/11362"
# r = requests.get(URL, auth=cr2, headers={"Content-Type": "application/json"})
# print(r.json())

URL = "https://testrail.dwos.com//index.php?/api/v2/get_cases/2&section_id=11362"
r = requests.get(URL, auth=cr2, headers={"Content-Type": "application/json"})
for i in r.json():
    print(i)