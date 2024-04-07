from django.db import models
class User_manager(models.Model):
    User_id = models.IntegerField(max_length=255, db_column="User_id", primary_key=True, null=False, auto_created=True)
    User_name = models.CharField(max_length=255, db_column="User_name")
    User_Permission = models.IntegerField(db_column="User_Permission")
    User_account = models.CharField(max_length=255, db_column="User_Account")
    User_Password = models.CharField(max_length=255, db_column="User_Password")
    User_mail = models.CharField(max_length=255, db_column="User_mail")
    User_Zone = models.CharField(max_length=255, db_column="User_zone")
    class Meta:
        db_table = "User_manager"
