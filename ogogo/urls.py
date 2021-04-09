from django.urls import path
from .views import *

urlpatterns = [
    path('', RegisterView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('certification/',ProfileView.as_view()),
    path('day/',DayView.as_view()),
    path('schedule/',ScheduleView.as_view()),
    path('service_time/',ServiceTimeView.as_view()),
    path('service/',ServiceView.as_view()),
    path('order/',OrderAPIView.as_view()),

]