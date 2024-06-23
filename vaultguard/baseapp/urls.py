from django.urls import path
from baseapp import views

urlpatterns = [
    path('',views.homeView,name='home'),
    path('base/',views.baseView),
    path('comingsoon',views.comingsoonView,name='comingsoon'),
    path('check_session/', views.check_session, name='check_session'),
]
