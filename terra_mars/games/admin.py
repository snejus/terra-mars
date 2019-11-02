from django.contrib import admin

from games import models

admin.site.register(models.Player)
admin.site.register(models.Corporation)
admin.site.register(models.Game)
admin.site.register(models.PlayerGameStats)
