from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView)
from .models import Post


def home(request):
	context ={
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html',context)

class PostListView(ListView):
	# model variable will define what model to query to create the kist	
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	# -date_posted will make sure that the newest posts remain at the top 
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	# model variable will define what model to query to create the kist	
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	# model variable will define what model to query to create the kist	
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

def about(request):
	return render(request, 'blog/about.html',{'title': 'About'})