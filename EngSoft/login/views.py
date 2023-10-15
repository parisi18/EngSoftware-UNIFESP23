from django.shortcuts import render

# Create your views here.
def load_login(request):
    return render(request, 'login.html')