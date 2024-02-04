from django.urls import path
from user import views

urlpatterns = [
    path('user/', views.user_data),
    path('user/<str:name>/', views.user_name),
    path('user/<str:name>/update', views.update_user_name),  
]

