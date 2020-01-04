from django.urls import path
from .views import *

app_name = 'friends'

urlpatterns = [
    
    path('', friends_list, name='friends_list'),
    
]