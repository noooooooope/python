from django.contrib import admin
from django.urls import include, path
from blog.views import blog_list
from django.conf.urls.static import static
from .import views

urlpatterns=[
     path('',views.blog_list,name='blog_list'),
     path('<int:blog_pk>',views.blog_detail,name="blog_detail"),
     path('type/<int:blog_type_pk>',views.blog_with_type,name="blog_with_type"),
     path('login/',views.login,name='login'),
     

]

