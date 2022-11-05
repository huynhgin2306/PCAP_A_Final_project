from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate
def index(request):
    return render(request, 'myapp/home.html')
def login(request):
    return render(request, 'myapp/login.html')
def account(request):
    return render(request, 'myapp/account.html')
def aboutus(request):
    return render(request, 'myapp/aboutus.html')
# Create your views here.
class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>HAHA</h1>')
    
class LoginClass(View):
    def get(self, request):
        return render(request,'myapp/login.html')
    def post(self, request):
        user_name = request.POST.get('user')
        passw = request.POST.get('password')
        my_user = authenticate(username=user_name, password=passw )
        if my_user is None:
            return render(request, 'myapp/account.html')
        return HttpResponse('dang nhap that bai')
    