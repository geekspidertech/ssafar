### -*- coding: utf-8 -*- ####################################################
from django import template 
register = template.Library()
import logging
from django.conf import settings


from ..models import CategoryList


@register.inclusion_tag('categoryList_source.html')
def get_category(slug):
    slug_name=slug
    category = CategoryList.objects.get(slug__exact=slug_name)
    return {
                'category': category, 'size': "%ix%i" % (int(category.width), int(category.height)),
                'width': category.width, 'height': category.height,
                'STATIC_URL': settings.STATIC_URL,
    }

#For correct image 
get_category.function= True
