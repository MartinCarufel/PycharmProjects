import json
import requests
from requests.auth import HTTPBasicAuth

def nice_dict_display(dict):
    for item in dict:
        for label, value in item.items():
            print(f"{label} : {value}")
        print("-------------------------")

URL = 'https://restful-booker.herokuapp.com'
credential = HTTPBasicAuth('admin', 'password123')
api_token = requests.post(URL+"/auth", data={"username": "admin", "password": "password123"})

r = requests.get(URL+"/booking").json()
# print(r)

# print(api_token.text)

book_listing = []
# book_listing.append(requests.get(URL+"/booking/"+str(145)).json())
# for idx in range(0, 20):
print(len(r))
for idx in range(len(r)-1, 0, -1):
    # book_listing.append(requests.get(URL+"/booking/"+str(item["bookingid"])).json())
    book_listing.append(requests.get(URL + "/booking/" + str(r[idx]["bookingid"])).json())
#
# print(book_listing)
nice_dict_display(book_listing)
