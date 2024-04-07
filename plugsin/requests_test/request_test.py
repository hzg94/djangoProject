import requests
import time
import ujson

from plugsin.requests_test.data_upload_mysql import data_to_mysql


def get_data(number):
    app_key = "Sgx2n0pGPIWEgtAwL"
    url = "https://api.seniverse.com/v3/weather/daily.json?key=" + app_key + "&location=" + str(
        number) + "&language=zh-Hans&unit=c&start=0&days=15"
    res = requests.get(url, timeout=50000)
    return res.text


def get_data_mysql():
    with open("plugsin/requests_test/citydata.json", 'r', encoding="utf-8") as f:
        data = ujson.loads(f.read())
    loading = 0
    for d in data:
        with open("plugsin/requests_test/res/" + str(d["id"]) + ".json", 'w', encoding="utf-8") as f:
            f.write(get_data(d["id"]))
        time.sleep(3.4)
        print(d["name"])
        print(len(data) - loading)
        loading += 1
    data_to_mysql()
