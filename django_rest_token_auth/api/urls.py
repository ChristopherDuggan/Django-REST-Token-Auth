from django.urls import path
from . import views

urlpatterns = [
    path('cats-list/', views.cats_list, name='cats_list'),
    # path('cats-list/', views.CatsView.as_view(), name='cats_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]


