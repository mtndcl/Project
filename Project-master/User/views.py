from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.core.mail import send_mail

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

            messages.warning(request, 'Your username/password is wrong or your account is not active yet.')
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
    
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('mail')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        


        try:
            user = User.objects.get(username=username)
            messages.warning(request, 'The username you entered has already been taken. Please try another username.')
            return HttpResponseRedirect(reverse('register-page'))
        except :      
            if password and password2 and password != password2:
                messages.warning(request, 'Passwords does not match! ')
                return HttpResponseRedirect(reverse('register-page'))

            elif password == password2 :  
                user = User.objects.create_user(username)
                user.is_staff = True 
                user.is_active = False 
                user.set_password(password)
                user.save()
                mail_message = '\nFirst Name : ' + name + '\nLast Name : ' + surname + '\nUsername : ' + username +  '\nE-mail : ' + email + '\nPhone Number : ' + phone_number 
                send_mail('Account Approval Required',
                mail_message,
                'design.project.focus@gmail.com',
                [email],
                fail_silently=False)
                return render(request, 'User/information.html')
    return render(request, 'User/register.html', {})


