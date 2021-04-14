from django.urls import path
from .views import *

urlpatterns = [
    path('vip/',VipView.as_view()),
    path('', AuthorizationView.as_view()),
]
