import json
a={'4': 5,'6': 7,'1': 3,'2': 4}
with open("que4.json","w") as f:
    a=json.dump(a,f,sort_keys=True)
