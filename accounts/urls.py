from django.urls import path

from . import views

 

urlpatterns = [
  path('login/', views.user_login, name='login')
  # path('', views.index, name='home'),
  # path('search-product;', views.search_product, name='search-product'),
  # path('add-product/', views.add_product, name='add-product'),
  # path('sell-product/<int:id>', views.sell_product, name='sell-product'),
  # path('delete-product/<int:id>', views.delete_product, name='delete-product'),
  # path('product-detail/<int:id>', views.product_detail, name='product-detail'),

]