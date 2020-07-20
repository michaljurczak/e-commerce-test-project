from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import main_view, cart_view, search_view, category_view, item_detail_view, add_product_view, \
        add_to_cart_view, delete_order_view, manage_orders_view, update_order_view
from authentication.views import login_view, register_view, logout_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register_view, name='register_view'),
    path('search/', search_view, name='search_view'),
    path('add-product/', add_product_view, name='add_product_view'),
    path('delete-order/<int:order_id>', delete_order_view, name='delete_order_view'),
    path('manage-orders/', manage_orders_view, name='manage_orders_view'),
    path('update-order/<int:order_id>', update_order_view, name='update_order_view'),
    path('category/<str:category>', category_view, name='category_view'),
    path('category/<str:category>/<slug:slug>', item_detail_view, name='item_detail_view'),
    path('cart/', cart_view, name='cart_view'),
    path('add_to_cart/<str:product_name>', add_to_cart_view, name='add_to_cart_view'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="authentication/reset_password.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/token/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
