from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from .models import Place, Image


# admin.site.register(Place)
admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    sortable_by = ('id',)
    # raw_id_fields = ('id',)
    # fields = ('id',)
    # raw_id_fields = ('place',)


@admin.register(Place)
class UserAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
