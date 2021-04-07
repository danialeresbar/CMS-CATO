from django.utils.translation import ugettext_lazy as _
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

from presentation import constants as c

CONTENT = _('Content management')
SETTINGS = _('Tools')
IMPORT_EXPORT_LANGUAGE = _("Import-export data from post's language")


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem(c.USER, icon='fa fa-user', children=[
            ChildItem(model='auth.user'),
            ChildItem(model='auth.group'),
        ]),
        ParentItem(c.MENU, icon='fa fa-bars', children=[
            ChildItem(model='menus.menu'),
            ChildItem(model='menus.menuitem'),
        ]),
        ParentItem(CONTENT, icon='fa fa-sitemap', children=[
            ChildItem(model='contents.page'),
            ChildItem(model='contents.generaldata'),
            ChildItem(model='contents.section'),
            ChildItem(model='contents.post'),
            ChildItem(model='contents.bannergallery'),

            ChildItem(model='contents.contact'),
        ]),
        ParentItem(SETTINGS, icon='fa fa-cogs', children=[
            ChildItem(model='tools.language'),
            ChildItem(model='contents.tag'),
            ChildItem(model='contents.sectiontemplate'),
            ChildItem(model='contents.postlanguage', label=IMPORT_EXPORT_LANGUAGE)

        ])
    )
