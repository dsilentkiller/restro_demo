
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'user'

urlpatterns = [


    path('login', views.login, name='user_login'),
    path('sign-up/', views.sign_up, name='sign-up'),

]
