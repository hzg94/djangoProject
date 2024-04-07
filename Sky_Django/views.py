import os
import pymysql
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from djangoProject import settings
from plugsin.knn_run import knntest
from plugsin.requests_test import request_test

scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
scheduler.add_jobstore(DjangoJobStore(), "default")
try:
    def my_job():
        request_test.get_data_mysql()
        knntest.knn_test()
    def jar_job():
        mysql_setting = settings.DATABASES["default"]
        connect = pymysql.connect(host=mysql_setting["HOST"], port=mysql_setting["PORT"], user=mysql_setting["USER"],
                              password=mysql_setting["PASSWORD"], db=mysql_setting["NAME"])
        curror = connect.cursor()
        curror.execute("delete from dataChange")
        connect.commit()
        connect.close()
        # os.system("java -jar plugsin/test/unit/jar/jar/weather-1.0-SNAPSHOT-jar-with-dependencies.jar 172.18.38.32 "
        #           "weather01 root 123456")
    def task_min():
        print()
    scheduler.add_job(task_min, "cron", second=1, id="task")
    scheduler.add_job(jar_job, "cron", minute=4, id="task_time", timezone="Asia/Shanghai")
    scheduler.add_job(my_job, "cron", minute=4, id="task_time", timezone="Asia/Shanghai")
    scheduler.start()
except Exception as e:
    print(e)
    scheduler.shutdown()
