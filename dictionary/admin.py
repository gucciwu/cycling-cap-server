from django.contrib import admin
from .models import Dictionary
from base.admin import BaseModelAdmin


class DictionaryModelAdmin(BaseModelAdmin):
    list_display = ('entry', 'key', 'value') + BaseModelAdmin.list_display


admin.site.register(Dictionary, DictionaryModelAdmin)
