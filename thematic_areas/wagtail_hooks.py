from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

from wagtail.contrib.modeladmin.views import CreateView
from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register, ModelAdminGroup)

from .models import ThematicArea


class ThematicAreaCreateView(CreateView):

    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class ThematicAreaAdmin(ModelAdmin):
    model = ThematicArea
    create_view_class = ThematicAreaCreateView
    menu_label = _('Thematic Area')
    menu_icon = 'folder'
    menu_order = 100
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('level0', 'level1', 'level2', 'creator',
                    'updated', 'created', )
    search_fields = ('level0', 'level1', 'level2', )
    list_export = ('level0', 'level1', 'level2', 'creator',
                   'updated', 'created', )
    export_filename = 'thematic_areas'


modeladmin_register(ThematicAreaAdmin)
