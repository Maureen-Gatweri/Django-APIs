# # from django.shortcuts import render

# # Create your views here.
# # from pyexpat.errors import messages
# from django.contrib import messages
# from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login ,logout
# # from django.contrib import messages
# # Create your views here.
# def user_login(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username,password=password)

#         if user is not None:
#             login(request, user)
#             redirect('home')
#             # return '/student/'
#         else:
#             messages.error(request, 'invalid username or password')
#     return render(request, 'accounts/login.html')
# def user_logout(request):
#     logout(request)
#     return redirect('login')

# # def home_view(request):
# #     return render(request, 'accounts/home.html')


from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib import messages
from accounts.views import login

def login(request):
    if request.method=="POST":
        username= request.Post["username"]
        password=request.Post["password"]
        user= authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            redirect("home")
        else:
            messages.error(request, 'Invalid username or password')
    return render (request, ' accounts/login.html')
def logout(request):
    logout(request)
    return redirect('login')