str = "晴天 : 58.0%,雨 : 15.0%,多云 : 7.0%,雪 : 8.0%,毛毛雨 : 9.0%"

strl = str.split(',')

for i in strl:
    print(i.split(":")[0])
    print(float(i.split(":")[1][1:-1]))
