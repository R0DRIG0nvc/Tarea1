from django.contrib import admin
from basket.models import *

# Register your models here.
# admin.site.register(Team)
# admin.site.register(Player)
# admin.site.register(Couch)
# admin.site.register(Match)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
    # list_display = ( 'logo' )
    # list_filter = ( 'name' )

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_filter_horizontal = ('birthdate', 'team') # no funciona 
    # list_filter = ( 'name', 'nickname', 'rut')
