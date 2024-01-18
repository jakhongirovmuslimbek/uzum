from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('products.urls')),

    # swagger urls
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
