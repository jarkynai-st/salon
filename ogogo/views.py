from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views,status
from .serializer import *


class ProfileView(views.APIView):
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data)


class CertificationView(views.APIView):
    def get(self, request, *args, **kwargs):
        certification = Certification.objects.all()
        serializer = CertificationSerializer(certification,many=True)
        return Response(serializer.data)


class DayView(views.APIView):
    def get(self, request, *args, **kwargs):
        day = Day.objects.all()
        serializer = DaySerializer(day,many=True)
        return Response(serializer.data)


class ScheduleView(views.APIView):
    def get(self, request, *args, **kwargs):
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule,many=True)
        return Response(serializer.data)


class ServiceTimeView(views.APIView):
    def get(self, request, *args, **kwargs):
        service_time = ServiceTime.objects.all()
        serializer = ServiceTimeSerializer(service_time,many=True)
        return Response(serializer.data)


class ServiceView(views.APIView):
    def get(self,request,*args,**kwargs):
        service = Service.objects.all()
        serializer = ServiceSerializer(service,many=True)
        return Response(serializer.data)


class OrderAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response({
                    "id": 1,
                    "service": 1,
                    "service_time": "free",
                    "date_created": "2021-04-07T17:49:28.748633+06:00",
                    "user": 1,
                        })


class RegisterView(views.APIView):

    def get(self,request,*args,**kwargs):
        users = User.objects.all()
        serializer = RegisterSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
