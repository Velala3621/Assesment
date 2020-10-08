from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.loginview, name='login'),
    path('product/list/', views.productlist.as_view(), name='product-list'),
    path('product/add/', views.ProductItemCreate.as_view(), name='product-add'),
    path('product/<int:pk>', views.ProductItemUpdate.as_view(), name='product-update'),
    path('product/<int:pk>', views.ProductDelete.as_view(), name='product-delete'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)