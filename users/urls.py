from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user-list'),
    path('users/create/', views.user_create, name='user-create'),
    path('users/update/<int:pk>/', views.user_update, name='user-update'),
    path('users/delete/<int:pk>/', views.user_delete, name='user-delete'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('users/',views.user_view),             
    path('users/<int:pk>/', views.user_view),
]