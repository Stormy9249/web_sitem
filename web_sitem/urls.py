from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ana_sayfa.urls')),
    path('admin/', admin.site.urls),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
