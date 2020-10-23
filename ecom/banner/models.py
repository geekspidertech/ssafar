### -*- coding: utf-8 -*- ####################################################

import random

from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.fields import ImageField 

from .utils import default_upload_to

class Banner(models.Model):

    slug = models.SlugField(_("Unique identifier"), unique=True)
    image = ImageField(_(u"Banner's image"), max_length=255, upload_to=default_upload_to, blank=True)
    link = models.CharField(_("External link"), max_length=255, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True)
    desc = models.CharField(max_length=100, blank=True)
    cta_text = models.CharField(max_length=15, blank=True)
    width = models.CharField(max_length=4, blank=True)
    height = models.CharField(max_length=4, blank=True)
    img_only = models.BooleanField(default=False)
    class Meta:
        ordering = ('slug',)
        verbose_name = _("banner")
        verbose_name_plural = _("banners")
    
    def __unicode__(self):
        return u"Banner: %s" % self.slug
    
    def get_image(self):
        """Returns random image using alternatives"""
        images = []
        if self.image:
            images.append(self.image)
        
        images.extend([i.image for i in self.alternatives.all()])
        
        return random.choice(images) if images else ''

class AlternativeImage(models.Model):
    
    banner = models.ForeignKey(Banner, verbose_name=_("banner"), related_name="alternatives" ,on_delete=models.CASCADE)
    image = ImageField(_("image"), upload_to=default_upload_to)
    
    class Meta:
        verbose_name = _("alternative image")
        verbose_name_plural = _("alternative images")
