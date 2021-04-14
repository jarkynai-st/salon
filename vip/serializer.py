from rest_framework import serializers
from .models import Vip, Authorization




class VipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vip
        fields = '__all__'


class AuthorizationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Authorization
        fields = ['username','password']
