from django.contrib import admin

# Register your models here.
from .models import Player, Team

admin.site.register(Team)
admin.site.register(Player)
