from django.urls import path

from core import views

urlpatterns = [
    path('signup', views.RegistrationView.as_view(), name='signup'),
    # path('profile', views.______View.as_view(), name='profile'),
    # path('login', views..______View.as_view(), name='login'),
    # path('update_password', views..______View.as_view(), name='update_password'),
]
