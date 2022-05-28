from django.shortcuts import render

# Create your views here.
def accounts(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')
