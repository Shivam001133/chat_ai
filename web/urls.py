from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('login-page/', views.login_page_view, name='login-page'),
    path('new-login-page/', views.new_login, name='new-login-page'),
    re_path('profile-page/int:id/', views.profile_page_view, name="profile-page"),  

]