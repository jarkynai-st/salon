from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    image = models.ImageField(blank=True,null=True)
    full_name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    date_start = models.DateField(auto_now_add=True)
    gender = models.CharField(choices=(
        ('woman','woman'),
        ('men','men'),
    ),max_length=20)
    service = models.ForeignKey('Service',on_delete=models.SET_NULL,null=True,related_name='profile')
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,related_name='profile')


class ProfileMaster(models.Model):
    image = models.ImageField(blank=True,null=True)
    full_name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    gender = models.CharField(choices=(
        ('woman', 'woman'),
        ('men', 'men'),
    ), max_length=20)


class Certification(models.Model):

    course_name = models.CharField(max_length=30)
    date = models.DateField()
    photo = models.ImageField(blank=True,null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True,related_name='certification')


class Day(models.Model):
    name = models.CharField(choices=(
        ('monday','monday'),
        ('wednesday','wednesday'),
        ('friday','friday'),
    ),max_length=50)


class Schedule(models.Model):
    day = models.ForeignKey(Day,on_delete=models.SET_NULL,null=True,related_name='schedule')
    time = models.DateTimeField()


class ServiceTime(models.Model):
    schedule = models.ForeignKey(Schedule,on_delete=models.SET_NULL,null=True,related_name='service_time')
    service = models.ForeignKey('Service',on_delete=models.SET_NULL,null=True,related_name='service_time')
    status = models.CharField(choices=(
        ('free','free'),
        ('busy','busy'),
    ),max_length=15)


class Service(models.Model):
    name = models.CharField(max_length=50)
    order_count = models.PositiveIntegerField()
    price = models.PositiveIntegerField(default=0)


class Order(models.Model):
    service = models.ForeignKey(Service,on_delete=models.SET_NULL,null=True,related_name='order')
    service_time = models.ForeignKey(ServiceTime,on_delete=models.SET_NULL,null=True,related_name='order')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True,related_name='order')


