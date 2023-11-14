from django.urls import path

from . import views


urlpatterns = [
    path('user-create/', views.UserCreateApiView.as_view()),
    path('user-list/', views.UserListApiView.as_view()),
]
