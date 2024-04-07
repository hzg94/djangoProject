import joblib
import numpy as np
import pymysql
import time

from djangoProject import settings


def knn_test():
    mysql_setting = settings.DATABASES["default"]
    connect = pymysql.connect(host=mysql_setting["HOST"], port=mysql_setting["PORT"], user=mysql_setting["USER"],
                              password=mysql_setting["PASSWORD"], db=mysql_setting["NAME"])
    currors = connect.cursor()
    currors.execute("select New_city_id, Old_city_id from newlinkold")
    data = currors.fetchall()
    for i in data:
        now_time = time.strftime("%Y-%m-%d", time.localtime())
        model = joblib.load("plugsin/knn/{0}.pkl".format(i[1]))
        currors.execute("select * from today_data where city_id ='{0}' and date = '{1}'".format(i[0], now_time))
        city_data = currors.fetchone()
        knn_data = [city_data[3] + city_data[4], city_data[5], round(float(city_data[7]) / 3.6, 3),
                    city_data[4], city_data[3]]
        X_wine_test = np.array([knn_data])
        over = model.predict(X_wine_test)
        currors.execute("update knn_data set Rain_over= '{1}' where New_city_id='{0}'".format(i[0], over[0]))
        connect.commit()
    connect.close()
