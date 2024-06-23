from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def baseView(request):
    return render(request,'baseapp/base.html')

def homeView(request):
    return render(request,'baseapp/home.html')

def comingsoonView(request):
    return render(request,'baseapp/comingsoon.html')

def check_session(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True})
    else:
        return JsonResponse({'authenticated': False})