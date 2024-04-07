import os
import ujson
dd = os.listdir("./res")
shengfen = []
for d in dd:
    with open("res/" + d, 'r', encoding="utf-8") as f:
        dc = ujson.loads(f.read())
    if "status" not in dc:
        shengfen.append(dc["results"][0]["location"]["name"])
print(len(shengfen))
