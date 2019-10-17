from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages



def login_page(request):
    

    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request,username=username, password=password)

        
        if user is not None:

            print('The user logged in system')
            login(request, user)

            return HttpResponseRedirect(reverse('profile-page'))
        else:

            messages.warning(request, 'Your username or password wrong')
            print('failed log in')
            return HttpResponseRedirect(reverse('login-page'))
    else:
        print('log in show up')
        return render(request, 'User/login.html', {})
    
    
def profile_page(request):
    
    print('profile page show up')

    return render(request, 'User/profile.html')


def logout_page(request):
    


    logout(request)
    print('user log out')

    return HttpResponseRedirect(reverse('login-page'))


def register_page(request):
    
    print('register page show up')

    return render(request, 'User/register.html')