from django.urls import path
from . import views
from .views import IndexClass, LoginClass

app_name ='myapp'
urlpatterns = [
    path('', views.index),
    path('login.html/', LoginClass.as_view(), name='login'),
    path('account.html/', views.account, name='account'),
    path('aboutus.html/', views.aboutus, name='aboutus'),
]