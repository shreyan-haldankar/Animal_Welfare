from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    
    path('', views.home, name = "home"),
    path('profiles/', views.profiles, name="profiles"),
    path('gallery/', views.gallery, name="gallery"),
    path('donate/', views.donatePage, name="donate"),
        path('blog/', views.blog, name="blog"),
        path('blog-trial/', views.blogTrial, name="blog-trial"),

    path('donationSuccess/', views.donationSuccess, name="donationSuccess"),


    # path('login/', views.loginPage, name="login"),


]

