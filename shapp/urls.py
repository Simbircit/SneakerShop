from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='Sneakers'),
    path('<firm_name>', views.main_filtered, name='Sneakers'),
    path('add/<int:sneakers_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart')
]
