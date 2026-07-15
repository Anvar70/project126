from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserViews.as_view(), name='user-list'),
    path('users/create/', views.UserCreate.as_view(), name='user-create'),
    path('users/update/<int:pk>/', views.UserUpdate.as_view(), name='user-update'),
    path('users/delete/<int:pk>/', views.UserDelete.as_view(), name='user-delete'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]