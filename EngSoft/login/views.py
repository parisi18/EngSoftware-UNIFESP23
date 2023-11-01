from django.shortcuts import render

# Create your views here.
def load_login(request):
    return render(request, 'login.html')

def load_forgot_password(request):
    return render(request, 'forgot-password.html')

def load_new_password(request):
    return render(request, 'new-password.html')