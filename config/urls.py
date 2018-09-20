
#from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import serve

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^', include('modulos.inicio.urls', namespace='inicio')),

    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT } ),
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, }),
]
