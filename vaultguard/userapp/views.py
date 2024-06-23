from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password

# Create your views here.
def signupView(request):
    return render(request,'userapp/signin.html')

def handelSignup(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']

        if password1 == password2 :
            data = User.objects.filter(Q(email=email) | Q(username=username)) 
            if len(data) <=0:
                user = User.objects.create_user(username,email,password1)
                
                user1 = UserModel.objects.create(user=user)
                # user1.firstname = request.POST['firstname']
                # user1.lastname = request.POST['lastname']
                user1.save()

                return render(request,'userapp/login.html',{'messagekey':'Registration Successfull'})
            else:
                 # Render a message for existing user
                return render(request,'userapp/signin.html',{'messagekey':'User Already Exists'})
        else:
            context = {
                'username': username,
                'email': email,
                # 'firstname':firstname,
                # 'lastname':lastname
                
                # Do not include passwords in the context for security reasons
            }
            # Render a message for password mismatch
            return render(request,'userapp/signin.html',{'messagekey':'Password Does Not Match'},context)
    else:
        # Return a 404 response for non-POST requests
        return HttpResponse('404 - Not Found')

def LoginView(request):
    next = request.GET.get('next','')
    context = {
        'next':next,
        }
    return render(request,'userapp/login.html',context)

def handleLogin(request):
    if request.method == 'POST':
        loginemail = request.POST.get('email','')
        loginpassword = request.POST.get('pass','')
        
        # print(loginemail)
        # print(loginpassword)

        # user = authenticate(request, username=loginemail, password=loginpassword)
        try:
            user = User.objects.get(email=loginemail)
            print("user: ",user)
            if check_password(loginpassword,user.password):
                # login
                login(request,user)
                # request.session['user_id'] = user.id  #login manually
                print("user login ")
                next_url = request.POST.get('next','')
                print("next_url: ",next_url)
                if next_url:
                    return redirect(next_url)
                return redirect('password-list')
            else:
                print("password does not match!")
                return render(request,'userapp/login.html',{'messagekey':"Password does not match!"})
        except User.DoesNotExist:
            print("email not exist!")
            return render(request,'userapp/login.html',{'messagekey':"Email Does not Exist!"})
    return HttpResponse('404 - Not Found')

def logouthandle(request):
    logout(request)
    return redirect('home')
