### -*- coding: utf-8 -*- ####################################################

import random

from django.db import models
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.fields import ImageField 

from .utils import default_upload_to

class CategoryList(models.Model):

    slug = models.SlugField(_("Unique identifier"), unique=True)
    image = ImageField(_(u"Carousel's image"), max_length=255, upload_to=default_upload_to, blank=True)
    link = models.CharField(_("External link"), max_length=255, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True)
    desc = models.CharField(max_length=100, blank=True)
    cta_text = models.CharField(max_length=15, blank=True)
    width = models.CharField(max_length=4, blank=True)
    height = models.CharField(max_length=4, blank=True)
    img_only = models.BooleanField(default=False)


    class Meta:
        ordering = ('slug',)
        verbose_name = _("category")
        verbose_name_plural = _("categories")
    
    def __unicode__(self):
        return u"Category: %s" % self.slug
    
    def get_image(self):
        """Returns random image using alternatives"""
        images = []
        if self.image:
            imageProps = [self.image, self.cta_text, self.link, self.title, self.desc]
            images.append(imageProps)

        return images if images else ''




