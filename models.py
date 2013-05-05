from django.db import models
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase

class Gallery(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery_view', args=[self.pk])

    class Meta:
        verbose_name_plural = 'gallery'


class Picture(models.Model):
    gallery = models.ForeignKey(Gallery)
    image = models.ImageField(upload_to="uploads/images/")
    description = models.CharField(max_length=60)

class GalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(Gallery)
