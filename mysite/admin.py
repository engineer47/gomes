from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import Contact


class ContactAdmin(ModelAdmin):

    list_filter = ['created_date', ]

    list_display = ['created_date', 'name', 'email', 'phone', ]

    search_fields = ['phone', 'name', 'email', ]

admin.site.register(Contact, ContactAdmin)
