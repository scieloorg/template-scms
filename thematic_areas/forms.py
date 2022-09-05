from wagtail.admin.forms import WagtailAdminModelForm


class ThematicAreaForm(WagtailAdminModelForm):

    def save_all(self, user):
        thematic = super().save(commit=False)

        if self.instance.pk is not None:
            thematic.updated_by = user
        else:
            thematic.creator = user

        self.save()

        return thematic
