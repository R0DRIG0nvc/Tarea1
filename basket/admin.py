from django.contrib import admin
from basket.models import *

# Register your models here.
# admin.site.register(Team)
# admin.site.register(Player)
# admin.site.register(Couch)
# admin.site.register(Match)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'thumb' )
    search_fields = ('name', )
    def thumb(self, obj):
        return mark_safe("<img src='%s' width='40' height='40' >" % obj.logo.url)
    thumb.allow_tags = True
    thumb._name_ = 'Logo'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'nickname', 'rut')
    list_display = ( 'name' , 'thumb' , 'nickname')
    list_filter = ('name', 'birthdate')
    def thumb(self, obj):
        return mark_safe("<img src='%s' width='40' height='40' >" % obj.photo.url)
    thumb.allow_tags = True
    thumb._name_ = 'photo'

@admin.register(Couch)
class CouchAdmin(admin.ModelAdmin):
    pass

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass
