import json
from testrail import *



client = APIClient("https://testrail.dwos.com//")
client.user = "martin.carufel@dental-wings.com"
client.password = "4AhW6wYp0fRy3NoDgz8k-8.QqVxbWx88Am5feuTn1"

cases = client.send_get("get_cases/2/&section_id=11956")
print(type(cases))
print(cases)

