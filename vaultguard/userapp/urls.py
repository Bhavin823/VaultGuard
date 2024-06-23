from django.urls import path
from userapp import views

urlpatterns = [
    path('signup/',views.signupView,name='signup'),
    path('signuphandle',views.handelSignup,name='signuphandle'),
    path('login/',views.LoginView,name='login'),
    path('loginhandle/',views.handleLogin,name='loginhandle'),
    path('logouthandle',views.logouthandle,name='logouthandle')
    
]
