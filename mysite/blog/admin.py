from django.contrib import admin
from .models import BlogType,Blog

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
	lsit_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	lsit_display = ('title','blog_type','author','create_time','last_updated_time')