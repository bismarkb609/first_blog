from django.urls import path
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name="home-page"),
    #path('list_posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    path("sign_up/", views.sign_up, name="sign-up"),
    path("log_in/", views.log_in, name="log-in"),
    path("logout", views.logout, name="logout"),
    path("create_post/", views.create_post, name='create-post')
]


urlpatterns += staticfiles_urlpatterns()