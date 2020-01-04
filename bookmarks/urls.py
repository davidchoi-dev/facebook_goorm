from django.urls import path
from .views import *

app_name = 'bookmarks'

urlpatterns = [
    
    path('', bookmarks_list, name='bookmarks_list'),
    
]