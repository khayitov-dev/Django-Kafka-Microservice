from django.urls import path

from . import views

urlpatterns = [
    path('user-create/', views.UserCreateApiView.as_view(), name="user_create"),
    path('user-list/', views.UserListApiView.as_view(), name="user_list"),
    path('user-detail/', views.UserDetailsAPIView.as_view(), name="user_detail"),
    path('user-destroy/', views.UserDestroyApiView.as_view(), name="user_destroy"),
    path('user-update/', views.UserUpdateApiView.as_view(), name="user_update"),
]