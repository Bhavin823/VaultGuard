from django.shortcuts import render,redirect
from .models import PasswordVault,encrypt_passowrd,decrypt_password
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def passwordListView(request):
    passwordvault = PasswordVault.objects.filter(user=request.user)
    listdata = []
    for i in passwordvault:
        listdata.append({
            'id':i.id,
            'websitename':i.website,
        })
        
    context={
        "vault":passwordvault,
        "listdata":listdata,
    }

    return render(request,'vaultapp/password_list.html',context)

@login_required(login_url='login')
def AddPasswordView(request):
    return render(request,'vaultapp/addpassword.html')

@login_required(login_url='login')
def addPasswordHandleView(request):
    if request.method == "POST":
        site = request.POST.get('site','')
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        encrypted_password = encrypt_passowrd(password)
        
        vault = PasswordVault()
        vault.user = request.user
        vault.username_of_website = username
        vault.website = site
        vault.password_of_website = encrypted_password
        vault.save()
    
    return redirect('password-list')
@login_required(login_url='login')
def deletePasswordVIew(request,id):
    paswordVault = PasswordVault.objects.get(pk=id)
    paswordVault.delete()
    return redirect('password-list')

@login_required(login_url='login')
def passwordDetailView(request,id):
    passwordVault = PasswordVault.objects.get(pk=id)
    decrypted_password = decrypt_password(passwordVault.password_of_website)
    context = {
        'passwordDetail' :passwordVault, 
        'password_of_website':decrypted_password,  
    }

    return render(request,'vaultapp/password_detail.html',context)

@login_required(login_url='login')
def updatepasswordView(request,id):
    vault = PasswordVault.objects.get(pk=id)
    decrypted_passowrd = decrypt_password(vault.password_of_website)
    context={
        'passwordDetail':vault,
        'password_of_website':decrypted_passowrd,
    }

    return render(request,'vaultapp/updatepassword.html',context)

@login_required(login_url='login')
def updatePasswordHandleView(request,id):
    if request.method == "POST":
        vaultDetail = PasswordVault.objects.get(pk=id)

        vaultDetail.website = request.POST.get('site','')
        vaultDetail.username_of_website = request.POST.get('username','')
        updated_password = request.POST.get('password','')
        encrypted_password = encrypt_passowrd(updated_password)
        vaultDetail.password_of_website = encrypted_password

        vaultDetail.save()

        return redirect('password-detail',id)
