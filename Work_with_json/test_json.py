import json

with open("t.json") as fj:
    j = json.load(fj)
    print(j["name"], j['age'])


x = {'data': {'A':[10, 11, 12, 13], 'B':["Martin", "Julie"]}}

with open("js_obj.json", 'w') as f:
    json.dump(x, f)