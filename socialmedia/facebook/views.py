from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def login_page(request):

    return render(request, 'home.html')

def user_profile(request):
    user=request.user

    context={'user': user}
    return render(request, 'home.html', context)