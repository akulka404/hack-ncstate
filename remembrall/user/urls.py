from django.conf.urls import url
from user import views
from django.urls import path

urlpatterns = [
    url(r'^user/$', views.user_data),
    path('user/<str:name>/', views.user_name),
    path('user/<str:name>/update/', views.update_criminal),
]
