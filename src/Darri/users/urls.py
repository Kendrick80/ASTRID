from django.contrib import admin
from django.urls import path,include
from users.views import profile_view,chatbot_view,blog_view
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/',profile_view,name="profile"),
    path('home/',TemplateView.as_view(template_name='dashboard/home.html'),name='home'),
    path('blog/',blog_view,name="blog"),
    path('chatbot/',TemplateView.as_view(template_name='views/Chatbot.html'),name='chatbot'),
    path('blog/',TemplateView.as_view(template_name='views/blog.html'),name='blog'),
    path('Chatbot/',chatbot_view,name='chatbot'),
    path('login/',views.login_view,name="login"), 
    path('blog/',blog_view,name="blog"),
]
