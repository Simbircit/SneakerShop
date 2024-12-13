from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main, name='Sneakers'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('<firm_name>', views.main_filtered, name='Sneakers'),
    path('sneakers/<int:sneakers_id>', views.product, name='product'),
    path('add/<int:sneakers_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_one/<int:item_id>/', views.remove_one_from_cart, name='remove_one_from_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart')
]
