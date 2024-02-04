from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from sih23 import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import generate_token
from django.core.mail import EmailMessage,send_mail
from .models import storelogin
# Create your views here.

def showbussiness(r):
    return render(r,'home1.html')


def showstorelogin(r):
    if r.POST:
        print("HI")
        username = r.POST['username']
        pass1 = r.POST['pass1']

        user = authenticate(username = username,password = pass1)
        print(user)
        if user is not None:
            login(r,user)
            fname = user.first_name
            print(fname)
            return render(r,'home.html',{'fname1':fname})
        else:
            messages.error(r,"Wrond Credantials")
            return render(r,"index.html")
        
    return render(r,'signin1.html')

def showstoresignup(r):
    if r.POST:
        shopname = r.POST['shopname']
        shopno = r.POST['shopno']
        shopadd = r.POST['address']
        city = r.POST['city']
        district = r.POST['district']
        pincode = r.POST['pincode']
        contact = r.POST['contact']
        ownerfirstname = r.POST['ownerfirstname']
        ownersecondname = r.POST['ownersecondname']
        ownerusername = r.POST['ownerusername']
        email = r.POST['email']
        password = r.POST['password']
        confpass = r.POST['confirmpass']

        x = {'shopname':shopname,'shopno':shopno,'address':shopadd,'city':city,'district':district,'pincode':pincode,'contact':contact,'ownerfirstname':ownerfirstname,
             'ownersecondname':ownersecondname,'ownerusername':ownerusername,'email':email,'ownerpassword':password,'confirmpass':confpass}
        print(x)
        y = storelogin(x)
        y.save()










        sub = "welcome to Ewaste facility locator "
        message = "Hello" + myuser.first_name + "! \n" + "welcome to Ewaste facility locator!!" + "\n we have sent an email for the account confirmation, please confirm to activate your account.\n Thank you for visting our website!"
        from_email = settings.EMAIL_HOST_USER
        to = [myuser.email]
        send_mail(sub,message,from_email,to,fail_silently = True)
        return render(r,'signin1.html')
    return render(r,'signup1.html')

def storesignout(r):
    logout(r)
    messages.success(r,"You have successfully logged out")
    return render(r,"index.html")