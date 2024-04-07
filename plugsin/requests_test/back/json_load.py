import os
import ujson
def get_new_data():
    dd = os.listdir("C:\\Users\\asus\\Desktop\\python\\demotest\\djangoProject\\plugsin\\test\\requests_test\\res")
    str_list = []
    try:
        for c in dd:
            with open(
                    "C:\\Users\\asus\\Desktop\\python\\demotest\\djangoProject\\plugsin\\test\\requests_test\\res\\" + c,
                    'r', encoding="utf-8") as f:
                data = ujson.loads(f.read())
            if "status" not in data:
                for x in range(0, len(data["results"][0]["daily"])):
                    str1 = c[:-5] + ""
                    for i in data["results"][0]["daily"][0]:
                        str1 = str1 + "," + data["results"][0]["daily"][x][i]
                    str_list.append(str1)
        print(len(str_list) / 3)
    except Exception as e:
        print(e)
get_new_data()
