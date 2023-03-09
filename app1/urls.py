from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('yadav/',yadav,name='yadav'),
    path('friends/',friends,name='friends'),
]