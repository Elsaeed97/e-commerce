from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from django.core.paginator import Paginator 

# Create your views here.
def blog(request):
	posts_list = BlogPost.objects.order_by('-created_at')
	paginator = Paginator(posts_list, 6) # Show 6 per Page
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	context = {
		'posts':posts ,
	}
	return render(request,'blog/blog.html', context)

def post(request, post_id):
	post = get_object_or_404(BlogPost, pk=post_id)
	comments = Comment.objects.order_by('-time')[:4]
	context = {
		'post': post,
		'comments': comments,
	}
	return render(request, 'blog/blog_detail.html',context)

def comment(request):

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		comment = request.POST['comment']
		# post_id = request.POST['post_id']

		coment = Comment(post=post,name=name,email=email,comment=comment)
		coment.save()
		return redirect('/blog/'+post_id)
