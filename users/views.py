from django.shortcuts import render, redirect
from .form import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created sucessfully please log in')
            return render('users/register.html')

    else:
        form = UserRegisterForm()
    context = {
        "form":form
        }
    return render(request, 'users/register.html', {"form": form})


def loginUser(request):
    loginForm = AuthenticationForm()
    if request.method == 'POST':
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(
                    request, f'{user} sucessfully logged in')
                return redirect('blog:blogPage')
            else:
                messages.error(request, "Unsuccessful login. Invalid information.")
        # else:
        #     messages.error(request,"Invalid username or password.")    
    loginForm = AuthenticationForm()
    return render(request, 'users/login.html', context={"loginForm":loginForm,} )



def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('pages:homepage')
