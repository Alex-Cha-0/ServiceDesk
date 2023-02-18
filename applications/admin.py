import hashlib
import os

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Email, Staff, Division, AuthUserGroups, AuthUser, AuthGroup, Attachments, MailSettings

from django import forms


class EmailSettingsForm(forms.ModelForm):
    class Meta:
        model = MailSettings
        fields = "__all__"
        # widgets = {
        #     'password': forms.PasswordInput(attrs={'placeholder': "the password will be encrypted"})
        # }

    def clean_password(self):
        if self.cleaned_data["password"] == "password":
            raise forms.ValidationError("very simply")
        return self.cleaned_data["password"]




class EmailAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'subject', 'sender_name', 'datetime_send', 'uid_division', 'open_order', 'close_order', 'specialist',
        'get_message')
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


class EmailSettings(admin.ModelAdmin):
    form = EmailSettingsForm
    list_display = ('id', 'host', 'port', 'user', 'password', 'use_tls')

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields["password"].label = "Inter password"
    #     return form


admin.site.register(Email, EmailAdmin)

admin.site.register(Staff, StaffAdmin)

admin.site.register(Division, DivisionAdmin)

admin.site.register(Attachments, AttachAdmin)

admin.site.register(MailSettings, EmailSettings)

admin.site.site_title = 'Менеджер заявок'
admin.site.site_header = 'Менеджер заявок'
