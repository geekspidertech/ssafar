### -*- coding: utf-8 -*- ####################################################

import random

from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.fields import ImageField 

from .utils import default_upload_to

class Carousel(models.Model):

    slug = models.SlugField(_("Unique identifier"), unique=True)
    image = ImageField(_(u"Carousel's image"), max_length=255, upload_to=default_upload_to, blank=True)
    link = models.CharField(_("External link"), max_length=255, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True)
    desc = models.CharField(max_length=100, blank=True)
    cta_text = models.CharField(max_length=15, blank=True)
    width = models.CharField(max_length=4, blank=True)
    height = models.CharField(max_length=4, blank=True)

    class Meta:
        ordering = ('slug',)
        verbose_name = _("carousel")
        verbose_name_plural = _("carousels")
    
    def __unicode__(self):
        return u"Carousel: %s" % self.slug
    
    def get_image(self):
        """Returns random image using alternatives"""
        images = []
        if self.image:
            imageProps = [self.image, self.cta_text, self.link, self.title, self.desc]
            images.append(imageProps)
        for alt_image in self.alternatives.all():
            imageProps = [alt_image.image, alt_image.cta_text, alt_image.link, alt_image.title, alt_image.desc ]
            images.append(imageProps)
        return images if images else ''

    def get_size(self):
        size = [self.width , self.height]
        return size



class AlternativeImage(models.Model):
    
    carousel = models.ForeignKey(Carousel, verbose_name=_("carousel"), related_name="alternatives" ,on_delete=models.CASCADE)
    image = ImageField(_("image"), upload_to=default_upload_to)
    link = models.CharField(_("External link"), max_length=255, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True)
    desc = models.CharField(max_length=100, blank=True)
    cta_text = models.CharField(max_length=15, blank=True)
    
    class Meta:
        verbose_name = _("alternative image")
        verbose_name_plural = _("alternative images")
