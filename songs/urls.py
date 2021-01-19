from songs.views import *
from django.urls import path

urlpatterns=[
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]