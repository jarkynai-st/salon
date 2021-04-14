from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import authentication
from .serializer import *
from rest_framework import exceptions
from django.contrib.auth.models import User

class VipView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            group = request.user.groups.all()[0].name.lower()
        except IndexError:
            return Response("Please authorize!")
        if group == 'manager':
            vips = Vip.objects.all()

        elif group == 'admin':
            vips = Vip.objects.filter(status='active', secret_level='limited')

        elif group in ['admin','manager','user']:
            vips = Vip.objects.filter(status='active',secret_level=['limited','unlimited','strongly'])

        elif group == 'admin':
            vips = Vip.objects.filter(status='active')

        serializers = VipSerializer(vips,many=True)
        return Response(serializers.data)

    def post(self,request,*args,**kwargs):
        serializers = VipSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"data":"Vip created successfully, your grace!"})
        return Response(serializers.errors)


class Authorization(views.APIView):

    def authorizate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)

