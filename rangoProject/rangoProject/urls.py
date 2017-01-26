from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
url(r'^$', views.index, name='index'),
 url(r'^about/$', views.about, name='about'),
url(r'^rango/', include('rango.urls')),
url(r'^admin/', admin.site.urls),
url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),

# above maps any URLs starting
# with rango/ to be handled by
# the rango application
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
