from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import GalleryPlugin
from django.utils.translation import ugettext as _

class CMSGalleryPlugin(CMSPluginBase):
    model = GalleryPlugin
    name = _("Gallery")
    render_template = "gallery/gallery.html"

    def render(self, context, instance, placeholder):
        context.update({
            'gallery':instance.gallery,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)

class CMSPlainGalleryPlugin(CMSPluginBase):
    model = GalleryPlugin
    name = _("Plain Gallery")
    render_template = "gallery/plain_gallery.html"

    def render(self, context, instance, placeholder):
        context.update({
            'gallery':instance.gallery,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSPlainGalleryPlugin)