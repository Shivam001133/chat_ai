from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('login-page', views.LoginPage.as_view(), name='login-page'),
    path('profile-page', views.ProfilePage.as_view(), name="profile-page"),  

]