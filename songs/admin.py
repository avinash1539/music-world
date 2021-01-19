from django.contrib import admin
from songs.models import Songs, Watchlater, History

admin.site.register(Songs)
admin.site.register(Watchlater)
admin.site.register(History)
