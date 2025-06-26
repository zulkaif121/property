from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
   path(settings.ADMIN_URL, admin.site.urls),

   path('api/user/', include('accounts.urls', namespace='accounts')),
   path('api/property/',include('properties.urls',namespace='properties'))


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)