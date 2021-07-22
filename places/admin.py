from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image

admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    sortable_by = ('id',)
    readonly_fields = ('show_image',)

    def show_image(self, obj):
        max_height = 200
        return format_html('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.image.url,
            width=obj.image.width / (obj.image.height / max_height),
            height=max_height
        ))


@admin.register(Place)
class UserAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
