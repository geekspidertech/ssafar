### -*- coding: utf-8 -*- ####################################################
from django import template 
register = template.Library()
import logging
from django.conf import settings


from ..models import Banner


@register.inclusion_tag('banner_source.html')
def get_banner(slug, width, height):
    slug_name=slug
    banner = Banner.objects.get(slug__exact=slug_name)
    return {
                'banner': banner, 'size': "%ix%i" % (width, height), 
                'width': width, 'height': height, 
                'STATIC_URL': settings.STATIC_URL,
    }

#For correct image 
get_banner.function= True
