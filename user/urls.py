from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.registration, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('my-profile/', views.my_profile, name="my_profile"),
    path('<str:username>/', views.user_profile, name="user_profile"),
]

