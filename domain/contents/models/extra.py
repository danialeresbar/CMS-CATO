from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.contents.constants import APP_LABEL, PATH_APP
from domain.main.models import Audit, LanguageAbstract
from domain.menus.models import Menu


PATH_SITE = 'site/'
PATH_SITE_LOGO = f'{PATH_APP}{PATH_SITE}logo'
ORDER = _('order')
FOOTER = _('Footer')
MAIN_MENU = _('Main menu')
SITE_LOGO = _('Site logo')
GENERAL_DATA = _('General data')
GENERAL_DATA_TRANSLATIONS = 'translations'
GENERAL_DATA_LANGUAGE = _('General data language')
GENERAL_DATA_LANGUAGE_PLURAL = _('General data languages')


class GeneralData(Audit):
    """

    """

    logo = models.ImageField(verbose_name=SITE_LOGO, upload_to=PATH_SITE_LOGO, blank=True)

    class Meta:
        ordering = ['-active', 'creation_date']
        verbose_name = GENERAL_DATA
        verbose_name_plural = GENERAL_DATA
        app_label = APP_LABEL

    def __str__(self):
        return GENERAL_DATA


class GeneralDataLanguage(LanguageAbstract):

    footer = RichTextField(verbose_name=FOOTER, blank=True)
    main_menu = models.ForeignKey(Menu, verbose_name=MAIN_MENU, on_delete=models.CASCADE, null=True)
    metadata = JSONField(blank=True, default=dict, encoder=DjangoJSONEncoder, editable=False)
    general_data = models.ForeignKey(GeneralData, related_name=GENERAL_DATA_TRANSLATIONS, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('language', 'general_data'),)
        verbose_name = GENERAL_DATA_LANGUAGE
        verbose_name_plural = GENERAL_DATA_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.general_data}-{self.language}'
