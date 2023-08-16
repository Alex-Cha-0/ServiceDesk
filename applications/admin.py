import hashlib
import os

from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import *
from .models import *

from django import forms


class ChatAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'chat_id', 'user_name', 'content', 'datetime_send', 'sender_id')


class EmailAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'subject', 'sender_name', 'datetime_send', 'uid_division', 'open_order', 'close_order', 'specialist')
    list_filter = ('sender_name', 'datetime_send', 'open_order', 'close_order')
    list_display_links = ('id', 'subject')
    search_fields = ('subject', 'sender_name')
    fields = ('id', 'subject', 'sender_name', 'datetime_send', 'open_order', 'close_order', 'specialist', 'get_message')
    readonly_fields = ('id', 'subject', 'sender_name', 'datetime_send', 'uid_division', 'get_message')
    save_on_top = True

    def get_message(self, obj):
        if obj.text_body:
            return mark_safe(obj.text_body)
        else:
            return '-'

    get_message.short_description = 'Текст заявки'


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'uid_division')


class DivisionAdmin(admin.ModelAdmin):
    list_display = ('uid', 'department', 'email_group')


class AttachAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_email', 'link')


class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = "createddate"
    list_display = ('orderid', 'createddate', 'ordernumber_id', 'comment')


class ThemesAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryChoiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'thema',)
    fields = ('category', 'thema',)


admin.site.register(Chat, ChatAdmin)

admin.site.register(CategoryChoice, CategoryChoiceAdmin)

admin.site.register(Thema, ThemesAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Email, EmailAdmin)

admin.site.register(Staff, StaffAdmin)

admin.site.register(Division, DivisionAdmin)

admin.site.register(Attachments, AttachAdmin)

admin.site.site_title = 'Менеджер заявок'
admin.site.site_header = 'Менеджер заявок'
