from django.db import models

# Create your models here.
class tbl_reg(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
class tbl_login(models.Model):
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
class tbl_item(models.Model):
    item_name=models.CharField(max_length=50)
    count=models.IntegerField()
    date=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
class tbl_booking(models.Model):
    item_name=models.CharField(max_length=50)
    item_id=models.CharField(max_length=50)
    count=models.DecimalField(max_digits=6,decimal_places=2)
    booking_date=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
class tbl_rented(models.Model):
    item_name=models.CharField(max_length=50)
    item_id=models.CharField(max_length=50)
    count=models.CharField(max_length=50)
    booking_date=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
