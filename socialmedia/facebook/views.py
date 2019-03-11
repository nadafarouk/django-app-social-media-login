from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
@login_required
def login_page(request):
    user = request.user

    context = {'user': user}
    return render(request, 'home.html')
