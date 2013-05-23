from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import Gallery, Picture, PictureGroup

class PictureInline(admin.StackedInline):
    model = Picture
    
class PictureGroupAdmin(admin.ModelAdmin):
    model = PictureGroup
    inlines = [PictureInline]

admin.site.register(PictureGroup, PictureGroupAdmin)

class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)