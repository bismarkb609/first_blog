from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="home-page"),
    path('list_posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    path("sign_up/", views.sign_up, name="sign-up"),
    path("log_in/", views.log_in, name="log-in")
]
