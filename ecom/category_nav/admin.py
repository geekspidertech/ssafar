### -*- coding: utf-8 -*- ####################################################


from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import CategoryList

from django.apps import AppConfig



class CategoryAdmin(AdminImageMixin, admin.ModelAdmin):

    list_display = ('slug', 'link')
    search_fields = ('slug', 'link')


admin.site.register(CategoryList)
