
from email.policy import default
from django.db import models

# Create your models here.
class Books(models.Model):
   book_id=models.AutoField(primary_key=True)
   book_name=models.CharField(max_length=255,null=True,blank=True)
   type_book=models.CharField(max_length=255,null=True,blank=True)
   price=models.CharField(max_length=255,null=True,blank=True)
   class Meta:
        db_table='books'
class users(models.Model):
    user_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=255,null=True,blank=True)
    lastname=models.CharField(max_length=255,null=True,blank=True)
    username=models.CharField(max_length=255,null=True,blank=True)
    class Meta:
        db_table='users'
class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=255,null=True,blank=True)
    book_id=models.IntegerField(null=True,blank=True)
    user_id=models.IntegerField(null=True,blank=True)
    class Meta:
        db_table='orders'



   