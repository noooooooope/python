from django.shortcuts import render_to_response, get_object_or_404, redirect,render
from .models import Blog
from django.contrib import auth 


def blog_list(request):
	context = {}
	context['blogs'] = Blog.objects.all()
	return render_to_response('blog_list.html',context)

def blog_detail(request,blog_pk):
	context = {}
	context['blog'] = get_object_or_404(Blog,pk=blog_pk)
	return render_to_response('blog_detail.html',context)

def blog_with_type(request,blog_type_pk):
	context = {}
	blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
	context['blogs'] = Blog.objects.filter(blog_type=blog_type)
	context['blog_type'] = blog_type
	return render_to_response('blog_with_type.html',context)

def login(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(request,username=username,password=password)
	if user is not None:
		auth.login(request,user)
		return redirect('')

