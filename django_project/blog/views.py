from django.shortcuts import render

posts = [
	{
		'author': 'Bharani',
		'title': 'FEM',
		'content': 'First post content',
		'date_posted': 'May 06, 2021'
	},
	{
		'author': 'Anusu',
		'title': 'Finance',
		'content': 'Her post content',
		'date_posted': 'May 05, 2021'
	}
]

def home(request):
	context ={
		'posts': posts
	}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html',{'title': 'About'})