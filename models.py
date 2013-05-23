# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase

class Gallery(models.Model):
#     parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery_view', args=[self.pk])

    class Meta:
        verbose_name_plural = u'Галереи'
        verbose_name = u'Галерея'

class PictureGroup(models.Model):
    gallery = models.ForeignKey(Gallery)
    name = models.CharField(max_length=512)
    description = models.CharField(blank=True, max_length=1024)

    class Meta:
        verbose_name_plural = u'Группы фото'
        verbose_name = u'Группа фото'
    
    def __unicode__ (self):
        return u'%s' % (self.name)
    
class Picture(models.Model):
    group = models.ForeignKey(PictureGroup)
    image = models.ImageField(upload_to="uploads/images/")
    name = models.CharField(max_length=512, blank=True)
    description = models.CharField(blank=True, max_length=512)

class GalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(Gallery)
    
    class Meta:
        verbose_name_plural = u'Фотофии'
        verbose_name = u'Фотография'