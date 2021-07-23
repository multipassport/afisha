from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index_page),
    path('places/<int:place_id>', views.show_place, name='places'),
    path('tinymce/', include('tinymce.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)