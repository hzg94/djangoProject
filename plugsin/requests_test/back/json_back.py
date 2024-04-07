import os
import ujson
ll = os.walk("./res")
ll = ll.__next__()[2]
back_city = []
for i in ll:
    with open("./res/" + i, 'rb') as f:
        temp = f.read().decode()
    data = ujson.loads(temp)
    if "status" not in data:
        back_city.append(
            {'id': data["results"][0]["location"]["id"],
             'name': data["results"][0]["location"]["name"]})
back_city = ujson.dumps(back_city)
with open("citydata.json", 'w', encoding="utf-8") as f:
    f.write(back_city)
