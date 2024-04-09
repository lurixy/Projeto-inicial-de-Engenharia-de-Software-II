from django.shortcuts import render, redirect

# importing view class from django.views
from django.views import View

#importing all models from app/models.py
from .models import *

from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def  get(self, request):
        return render (request, 'login.html')
    def post (self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha invalida'})
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
        

class IndexView(View):
    #defining get method
    def get(self, request):
        produtos = Produto.objects.all()
        imovel = Imovel.objects.all()
        context = {
            "imoveis": imovel,
                }        
        return render(request, 'index.html', context)
        #defining post method
    def post(self, request):
            pass
