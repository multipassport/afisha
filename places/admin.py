from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    sortable_by = ('id',)
    readonly_fields = ('show_image',)

    def show_image(self, photo):
        max_height = 200
        return format_html('<img src="{}" style="max-height:{}px" />'.format(
            photo.image.url,
            max_height
        ))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)
