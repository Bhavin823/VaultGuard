from django.urls import path
from vaultapp import views

urlpatterns = [

    path('password-list/',views.passwordListView,name='password-list'),
    path('passwordDetailView/<int:id>/',views.passwordDetailView,name='password-detail'),

    # form for make operation
    path('add-password/',views.AddPasswordView,name='add-password'),
    path('update-password/<int:id>',views.updatepasswordView,name='update-pasword'),

    # operation
    path('addpasswordhandle/',views.addPasswordHandleView,name='add-passwordhandle'),
    path('updatepasswordhandle/<int:id>/',views.updatePasswordHandleView,name='update-passwordhandle'),
    path('delete-password/<int:id>/',views.deletePasswordVIew,name='delete-password'),

]
