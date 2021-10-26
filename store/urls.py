from django.urls import path
from store import views

app_name = 'store'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    # function-based view
    # path('product/<int:pk>/', views.product_details, name='product-details'),
    # class-based view
    path('product/<slug>/', views.ProductDetailView.as_view(), name='product-details'),
]
