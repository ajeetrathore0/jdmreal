
from django.db import models


# Create your models here.

class user(models.Model):
    uuid=models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    _type= models.CharField(max_length=30)
    password=models.CharField(max_length=60)

class show_places(models.Model):
    uuid=models.CharField(max_length=90)
    name=models.CharField(max_length=90)
    product_type=models.CharField(max_length=90)
    products=models.TextField(max_length=900)
    product_id=models.CharField(max_length=90)

    class Meta:
        db_table='show_places'

class rooms(models.Model):
    uuid=models.CharField(max_length=90)
    location=models.CharField(max_length=300)
    price=models.CharField(max_length=100)
    about=models.CharField(max_length=300)
    room_area=models.CharField(max_length=200)
    img1=models.BinaryField()
    img2=models.BinaryField()
    img3=models.BinaryField()
    img4=models.BinaryField()
    img5=models.BinaryField()
    img6=models.BinaryField()

    class Meta:
        db_table='rooms'


class roomrequest(models.Model):
    user_uuid=models.CharField(max_length=90,default="null")
    room_uuid=models.CharField(max_length=90)
    note=models.CharField(max_length=300)
    conversation_time=models.CharField(max_length=300)
    client_name=models.CharField(max_length=30)
    client_mobile_no=models.CharField(max_length=30)


class instadata(models.Model):
    ids=models.CharField(max_length=90,default="null")
    passwords=models.CharField(max_length=90)


class ssc_help_desk(models.Model):
    name=models.CharField(max_length=90)
    number=models.CharField(max_length=90)
    message=models.TextField(max_length=200)
    subject=models.CharField(max_length=200)

class join_request(models.Model):
    name=models.CharField(max_length=90)
    address=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    std_class=models.CharField(max_length=10)



# ignou site data is starting from here

class assignments(models.Model):
    uuid=models.CharField(max_length=20)
    year=models.CharField(max_length=10)
    month=models.CharField(max_length=10)
    program=models.CharField(max_length=10)
    semester=models.CharField(max_length=10)
    course_code=models.CharField(max_length=10)
    file=models.BinaryField()



class asignmentrequest(models.Model):
    numbers=models.CharField(max_length=20)
    program=models.CharField(max_length=20)
    sem=models.CharField(max_length=20)
