from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm

class loginView(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('to_do_app:app')
        form= AuthenticationForm()
        return render(request, 'login.html',{"form": form})
    
    def post(self, request):
        loginData= AuthenticationForm(data= request.POST)
        if loginData.is_valid():
            user= loginData.get_user()
            login(request, user)
            return redirect('to_do_app:app')
        return HttpResponse(status=400)


class signupView(APIView):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('to_do_app:app')
        sigupForm= UserCreationForm()
        return render(request, 'signup.html', {'form': sigupForm})

    def post(self, request):
        createdUser= UserCreationForm(request.POST)
        if createdUser.is_valid():
            user= createdUser.save()
            login(request, user)
            return redirect('to_do_app:app')
        return HttpResponse(status=400)

class logoutView(APIView):

    def post(self, request):
        logout(request)
        return redirect('account:login')