
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_,name='login_'),
    path('register',views.register,name='register'),
    path('logout_',views.logout_,name='logout_'),
    path('profile',views.profile,name='profile'),
    path('resetpass',views.resetpass,name='resetpass'),

    path('update_profile',views.update_profile,name='update_profile'),

    path('logout',views.user_logout,name='logout_'),
  
]