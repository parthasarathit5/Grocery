from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/<int:product_id>/', views.add_to_cart),
    path('remove/<int:product_id>/', views.remove_from_cart),
    path('checkout/', views.checkout, name='checkout'),
     path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)