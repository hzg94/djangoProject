import pymysql
import ujson
connect = pymysql.connect(host="172.18.38.32", port=3306, user='root', password='123456', db="weather01")
currors = connect.cursor()
currors.execute("select * from num")
data1 = currors.fetchall()
connect.close()
city_data = []
with open('citydata.json', 'r', encoding="utf-8") as f:
    data = ujson.loads(f.read())
for i in data1:
    cc = i[3].replace('\n', '')
    if cc != "None":
        for xx in data:
            if xx["name"] in cc:
                city_data.append({
                    "city_id": i[0],
                    "new_city_id": xx['id'],
                    "city_name": xx['name']
                })
    else:
        for xx in data:
            if xx["name"] in i[2]:
                city_data.append({
                    "city_id": i[0],
                    "new_city_id": xx['id'],
                    "city_name": xx['name']
                })

connect = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="skyback_end")
currors = connect.cursor()
for i in city_data:
    sql = "insert into newLINKold (Old_city_id, New_city_id, city_name) values ({0}, '{1}','{2}')".format(i['city_id'],
                                                                                                          i[
                                                                                                              "new_city_id"],
                                                                                                          i[
                                                                                                              'city_name'])
    print(sql)
    currors.execute(sql)
    connect.commit()
connect.close()
