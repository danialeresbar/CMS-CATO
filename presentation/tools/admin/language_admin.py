from django.contrib import admin
from domain.entities.tools.models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    model = Language
    fields = ('name', 'abbreviation')