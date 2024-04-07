from django.db import models
class Zone_Data(models.Model):
    Old_city_id = models.IntegerField(max_length=11, db_column="Old_city_id", primary_key=True)
    New_city_id = models.CharField(max_length=100, db_column="New_city_id")
    city_name = models.CharField(max_length=100, db_column="city_name")
    class Meta:
        db_table = "newlinkold"
class Knn_data(models.Model):
    Rain_Over = models.IntegerField(max_length=10, db_column="Rain_over", primary_key=True)
    New_city_id = models.CharField(max_length=100, db_column="New_city_id")
    class Meta:
        db_table = "Knn_data"
class today_Data(models.Model):
    city_id = models.CharField(max_length=100, db_column="city_id", primary_key=True)
    city_name = models.CharField(max_length=100, db_column="city_name")
    text_day = models.CharField(max_length=100, db_column="text_day")
    high = models.IntegerField(max_length=11, db_column="high")
    low = models.IntegerField(max_length=11, db_column="low")
    humidity = models.IntegerField(max_length=11, db_column="humidity")
    rainfall = models.CharField(max_length=100, db_column="rainfall")
    wind_speed = models.CharField(max_length=100, db_column="wind_speed")
    date = models.CharField(max_length=100, db_column="date")
    class Meta:
        db_table = "today_data"
class noral_Data(models.Model):
    Old_city_id = models.CharField(max_length=100, db_column="Old_city_id", primary_key=True)
    New_city_id = models.CharField(max_length=100, db_column="New_city_id")
    city_name = models.CharField(max_length=100, db_column="city_name")
    data_date = models.CharField(max_length=100, db_column="data_date")
    data = models.CharField(max_length=100, db_column="data")
    class Meta:
        db_table = "dataChange"