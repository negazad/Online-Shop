from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'category'


urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('category/<slug:category_slug>/', views.HomeView.as_view(), name='category_filter'),
	path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

