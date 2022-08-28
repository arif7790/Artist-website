from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailsView.as_view(), name='product-detail'),

]

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)