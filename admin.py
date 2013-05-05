from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import Gallery,Picture

class PictureInline(admin.StackedInline):
    model = Picture

class GalleryAdmin(admin.ModelAdmin):
    inlines = [PictureInline]

admin.site.register(Gallery, GalleryAdmin)