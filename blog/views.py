from ctypes import create_unicode_buffer
import re
from venv import create
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Post, UserAccount
from .forms import SignUpform, Loginform, createPostForm
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def index(request):
    data = Post.objects.all()
    ctx = {"data": data}
    return render(request, "blog/index.html", ctx)

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
    
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def sign_up(request):
    signup_form = SignUpform()  
    if request.method == "POST":
        signup_form = SignUpform(request.POST)

        if signup_form.is_valid():
            firstName = signup_form.cleaned_data['firstName']
            lastName = signup_form.cleaned_data['lastName']
            userName = signup_form.cleaned_data['userName']
            email = signup_form.cleaned_data['Email']
            password = signup_form.cleaned_data['password']
            confirm_password = signup_form.cleaned_data['confirm_password']


        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect("")
            
            elif User.objects.filter(username=userName).exists():
                messages.info(request, "Username Already Used")
                return redirect("")

            else:
                UserAccount.objects.create(userName=userName, firstName=firstName, lastName=lastName, Email=email)
                user = User.objects.create_user(username=userName, password=password, first_name=firstName,  last_name=lastName, email=email)
                user.save()
                return redirect('log-in')

        else:
            messages.info(request, "Password Not the same")
        return HttpResponseRedirect("")

    else:
        signup_form = SignUpform()
        ctx = {
            'SignupForm': signup_form
        }
        return render(request, "blog/sign_up.html", ctx)



def log_in(request):
    login_form = Loginform()
    if request.method == "POST":
        login_form = Loginform(request.POST)

        if login_form.is_valid():
             userName = login_form.cleaned_data['userName']
             password = login_form.cleaned_data['password']


             user = auth.authenticate(username=userName, password=password)
             if user is not None:
                #means if authentication is successful 
                auth.login(request, user)
                return redirect('home-page')
             else:
                messages.info(request, "Account invalid")
                return redirect('sign-up')

    login_form = Loginform()
    ctx = {
        "loginForm" : login_form
    }
    return render(request, "blog/log_in.html", ctx)



def logout(request):
    auth.logout(request)
    return redirect("home-page")



def create_post(request):
    if request.method == "GET":
        createForm = createPostForm()
        return render(request, "blog/create_blog.html", {
            'form': createForm
        })
    else:
        createForm = createPostForm(request.POST)
        title = request.POST['title']
        text = request.POST['text']
        created_date = request.POST['created_date']

        Post.objects.create(title=title, text=text, created_date=created_date)
        return render(request, "blog/successful.html")