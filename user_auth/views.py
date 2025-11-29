from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        u=authenticate(username=username,password=password)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login_.html',{'status':True})
    
    return render(request,'login_.html')

                                                                                                                
def register(request):

    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        # logic for confirm password
        # task - put the login from password min 8 characters (upper,lower,number,specialchar)
        print(first_name,last_name,email,username,password)
        
        try :
            u=User.objects.get(username=username)
            return render(request,'register.html',{'status':True})

        except:
            u=User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
            )
            u.set_password(password)
            u.save()
            return redirect('login_')


    return render(request,'register.html')

@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html')

@login_required
def resetpass(request):

    u=User.objects.get(username=request.user)
    
    if request.method == 'POST':

        try:
            old_pass=request.POST['oldpass']
            verified = authenticate(username=u.username,password=old_pass)
            if verified:
                return render(request,'resetpass.html',{'verified':True})
            else:
                return render(request,'resetpass.html',{'not_verified':True})
        except:
            new_pass=request.POST['newpass']
            u.set_password(new_pass)
            u.save()
            return redirect('login_')

    return render(request,'resetpass.html')



@login_required
def update_profile(request):
    """
    Handles displaying and processing the form to update user details.
    """
    user = request.user
    
    if request.method == 'POST':
        # 1. Get updated data from the form
        user.username = request.POST['username']

        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        
        # 2. Save the changes to the database
        user.save()
        
        # 3. Redirect back to the profile page to show the updates
        return redirect('profile')
    
    # If it's a GET request, render the update form
    return render(request, 'update_profile.html', {'user': user})


def user_logout(request):
    logout(request)
    return redirect("login_")