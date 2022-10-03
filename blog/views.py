from cmath import log
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

from .forms import SignUpform, Loginform
# Create your views here.

def index(request):
    data = Post.objects.all()
    ctx = {"data": data}
    return render(request, "blog/index.html", ctx)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def sign_up(request):
    signup_form = SignUpform()
    ctx = {
        'SignupForm': signup_form
    }
    return render(request, "blog/sign_up.html", ctx)


def log_in(request):
    login_form = Loginform()
    ctx = {
        "loginForm" : login_form
    }
    return render(request, "blog/log_in.html", ctx)