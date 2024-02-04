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
# Create your views here.
def showindex(r):
    return render(r,'index.html')


def showhome(r):
    return render(r,'home.html')



def showuserlogin(r):
    if r.POST:
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
            return redirect(showindex)
        
    return render(r,'userlogin.html')

def showsignup(r):
    if r.POST:
        print(r)
        firstname = r.POST['firstname']
        secondname = r.POST['secondname']
        username = r.POST['username']
        phoneno = r.POST['phoneno']
        mail = r.POST['email']
        password = r.POST['password']
        confirmpass = r.POST['confirmpass']
        print(firstname,secondname)

        if User.objects.filter(username = username):
            messages.error(r,"Username already exists")
            return render(r,"signup.html")

        if len(username)>10:
            messages.error(r,"username must be less thatn 10 characters")
            return render(r,"signup.html")
        
        if password != confirmpass:
            messages.error(r,"Password didn't match")
            return render(r,"signup.html")
        
        if not username.isalnum():
            messages.error(r,"No characters other than numbers and alphabets are allowed")
            return render(r,"signup.html")
        
        

        myuser = User.objects.create_user(username,mail,password)
        myuser.first_name = firstname
        myuser.last_name = secondname
        myuser.contact = phoneno
        myuser.save()

        messages.success(r,"YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED")
        messages.success(r,"We have sent an email to confirm your account, Pls confirms to proceed further")

        #email

        sub = "welcome to Ewaste facility locator "
        message = "Hello" + myuser.first_name + "! \n" + "welcome to Ewaste facility locator!!" + "\n we have sent an email for the account confirmation, please confirm to activate your account.\n Thank you for visting our website!"
        from_email = settings.EMAIL_HOST_USER
        to = [myuser.email]
        send_mail(sub,message,from_email,to,fail_silently = True)
        return render(r,'userlogin.html')
    return render(r,'signup.html')

def signout(r):
    logout(r)
    messages.success(r,"You have successfully logged out")
    return render(r,"index.html")


def showuserdetails(r):
    if r.POST:
       username = r.POST['username']
       print(username)
       x = User.objects.filter(username = username).values_list('username','first_name','email')
       print(x)
       return render(r,"userdetails.html",{'values':x})

    return render(r,"userdetails.html")

def showprofile(r):
    return render(r,'profile.html')

def showshops(r):
     if r.POST:
        district = r.POST['district']
        y = storelogin.objects.filter(district = district).values_list('shopname','address','city','district','contact')
        return render(r,"shops.html",{'values':y})
     return render(r,'shops.html')