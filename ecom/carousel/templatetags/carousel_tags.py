### -*- coding: utf-8 -*- ####################################################
from django import template 
register = template.Library()
import logging
from django.conf import settings


from ..models import Carousel


@register.inclusion_tag('carousel_source.html')
def get_carousel(slug):
    slug_name=slug
    carousel = Carousel.objects.get(slug__exact=slug_name)
    return {
                'carousels': carousel, 'size': "%ix%i" % (int(carousel.width), int(carousel.height)),
                'width': carousel.width, 'height': carousel.height,
                'STATIC_URL': settings.STATIC_URL,
    }

#For correct image 
get_carousel.function= True
