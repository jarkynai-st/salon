import profile

from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.response import Response

from .models import *


class ProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = ['id','image','full_name','age','date_start','gender','user']


class CertificationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Certification
        fields = ['id','course_name','date','photo']





class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Day
        fields = ['name']


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ['day','time']


class ServiceTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceTime
        fields = ['schedule','status']


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['name','order_count','price']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id','service','service_time','date_created','user']


class RegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']


    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if confirm_password == password:
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.is_active = False
            user.save()

        return user