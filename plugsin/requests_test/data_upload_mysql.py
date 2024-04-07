import os
import pymysql
import ujson

from djangoProject import settings


def data_to_mysql():
    mysql_setting = settings.DATABASES["default"]
    connect = pymysql.connect(host=mysql_setting["HOST"], port=mysql_setting["PORT"], user=mysql_setting["USER"],
                              password=mysql_setting["PASSWORD"], db=mysql_setting["NAME"])
    currors = connect.cursor()
    ll = os.walk("plugsin/requests_test/res")
    ll = ll.__next__()[2]
    wait_data = []
    for i in ll:
        with open("plugsin/requests_test/res/" + i, 'r', encoding="utf-8") as f:
            data = ujson.loads(f.read())
        if "status" not in data:
            d_data = data["results"][0]["daily"]
            city_id = data["results"][0]["location"]['id']
            city_name = data["results"][0]["location"]['name']
            for x in d_data:
                wait_data.append({
                    "city_id": city_id,
                    "city_name": city_name,
                    "date": x["date"],
                    "text_day": x["text_day"],
                    "high": x["high"],
                    "low": x["low"],
                    "humidity": x["humidity"],
                    "rainfall": x["rainfall"],
                    "wind_speed": x["wind_speed"]
                })
    for i in wait_data:
        currors.execute("select * from today_data where date='{0}' and city_id = '{1}'".format(i["date"], i["city_id"]))
        if len(currors.fetchall()) > 0:
            data = "update today_data set text_day= '{0}', high ='{1}', low='{2}',humidity='{3}',rainfall='{4}'," \
                   "wind_speed='{5}' where city_id = '{6}' and date = '{7}'".format(
                i["text_day"], i['high'], i["low"],
                i["humidity"], i["rainfall"], i["wind_speed"], i["city_id"], i["date"])
        else:
            data = "insert into today_data (city_id, city_name, date, text_day, high, low,humidity,rainfall,wind_speed) " \
                   "values ('{0}', '{1}', '{2}', '{3}', '{4}' ,'{5}','{6}','{7}','{8}')".format(
                i["city_id"], i["city_name"], i["date"],
                i["text_day"], i['high'], i["low"],
                i["humidity"], i["rainfall"], i["wind_speed"])
        print(data)
        currors.execute(data)
        connect.commit()
    connect.close()
