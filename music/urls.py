"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from songs.views import search, playsong, home, watchlater, history, removewl, removehs

urlpatterns = [
    path('removehs/', removehs, name='removehs'),
    path('removewl/<int:song_id>',removewl,name='removewl'),
    path('history/',history,name='history'),
    path('watchlater/',watchlater,name='watchlater'),
    url('songs/',include('songs.urls')),
    path('',home,name='home'),
    path('playsong/<int:id>',playsong,name='playsong'),
    path('search/',search,name = 'search'),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
