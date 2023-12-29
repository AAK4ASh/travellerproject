from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# Create your views here.
def loginfun(request):
    if request.method=='POST':
        usernamelog=request.POST['usernamelogin']
        passwordlog=request.POST['passwordlogin']
        userdb = auth.authenticate(username=usernamelog, password=passwordlog)
        if userdb is not None:
            auth.login(request,userdb)
            print('error')
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            print('errorrrrrrr')
            return redirect('loginfun')

    return render(request,'login.html')
def credfun(request):
    if request.method=='POST':
        usernamed=request.POST['username']
        firstnamed=request.POST['firstname']
        lastnamed=request.POST['lastname']
        emaild=request.POST['email']
        passwordd=request.POST['password']
        cpasswordd=request.POST['cpassword']
        if passwordd==cpasswordd:
            if User.objects.filter(username=usernamed).exists():
                messages.info(request,'Username already taken.')
                print('username already taken')
                return redirect('credfun')

            elif User.objects.filter(email=emaild).exists():
                messages.info(request,'Account exists with this emailid')
                print('account exists with this emailid')
                return  redirect('credfun')
            else:
                user = User.objects.create_user(username=usernamed, first_name=firstnamed, last_name=lastnamed,
                                                email=emaild, password=passwordd)
                user.save()
                return redirect('loginfun')
        else:
            return redirect('/')
    return render(request,'cred.html')
def logoutfun(request):
    auth.logout(request)
    return redirect('/')
