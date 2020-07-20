from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import list_users, list_api, simple_list_users, list_user_detail, UserList, UserListMixins

urlpatterns = [
    path('', list_api, name='list_api'),
    path('users/', list_users, name='list_users'),
    path('users-cls/', UserList.as_view(), name='list_users_cls'),
    path('users-mxs/', UserListMixins.as_view(), name='list_users_mxs'),
    path('user/<int:pk>', list_user_detail, name='list_user_detail'),
    path('simple-users/', simple_list_users, name='simple_list_users'),
]

urlpatterns = format_suffix_patterns(urlpatterns)