from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('yadav/',yadav,name='yadav'),
    path('friends/',friends,name='friends'),
]