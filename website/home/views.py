from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model , authenticate , login , logout
from django.conf import settings
from .models import post
from django.core.files.storage import FileSystemStorage
import random

User = get_user_model()


def home(request):
    if request.user.is_authenticated:
        posted_by = str(request.user)
    else:
        posted_by = "Guest"
    if request.method == 'POST'  :
        t = posted_by
        comment = request.POST.get('comment')
        art = post(title=t,describtion=comment)
        if request.FILES :
            myfile = request.FILES['dbfile']
            fs = FileSystemStorage()
            art.img = fs.save(myfile.name, myfile)
            art.save()
        else:
             art.save()


    q = request.GET.get('q')
    query = post.objects.search(q)

    context={'posts':query}
    return render(request,'home/index.html', context)




#-login -- logout -- register
def logs(request):
    cs = str(request.user)
    if cs is not 'AnonymousUser':
        return redirect('home:home')
    context = None
    if request.method == 'POST':
        username = request.POST.get('Lusername')
        password = request.POST.get('Lpassword')
        user = authenticate(request,username=username,password=password)
        qs = User.objects.filter(username=username)
        if user is not None:
            login(request,user)
            #request.session.set_expiry(600)
            return redirect('home:logged')
        elif qs.exists() and user is None:
            x = "if you want reset your password please follow this link .";context={'passworderror':x}
        else:
            x = "username that you've entered doesn't match any account." ; context={'error':x}

    return render(request,'home/login.html',context)

def regs(request):
    c = str(request.user)
    if c is not 'AnonymousUser':
        return redirect('home:home')
    context = None
    if request.method == 'POST':
        Rusername = request.POST.get('Rusername')
        email = request.POST.get('Remail')
        password1 = request.POST.get('Rpassword1')
        password2 = request.POST.get('Rpassword2')
        qss = User.objects.filter(email=email)
        if password1 != password2 :
            x = "passwords have to match"; context={'passworderror':x}
        elif qss.exists():
            x = "there is an account with this email please write another one." ; context={'passworderror':x}
        else :
            new_user = User.objects.create_user(username=Rusername,email=email,password=password1)
            new_user.save()
            return redirect('home:logs')


    return render(request,'home/register.html',context)

def logsout(request):
    logout(request)

    return redirect('home:home')

#-profilepage
def prof(request):
    posted_by = str(request.user)
    context = {'username':posted_by}
    return render(request,'home/search.html',context)
def logged(request):


    return render(request,'home/home.html')

