from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
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

# LoginRequiredMixin - Makes sure that the user has logged in
class PostCreateView(LoginRequiredMixin, CreateView):
	# model variable will define what model to query to create the kist	
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

# UserPassesTestMixin - Make sures that the user who has created the post has the 
# power to update of delete the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	# model variable will define what model to query to create the kist	
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		# self.get_object() will get the post we want to edit
		post = self.get_object()
		# self.request.user = logged in user
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	# model variable will define what model to query to create the kist	
	model = Post
	success_url = '/'

	def test_func(self):
		# self.get_object() will get the post we want to edit
		post = self.get_object()
		# self.request.user = logged in user
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html',{'title': 'About'})