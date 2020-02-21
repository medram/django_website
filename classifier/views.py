from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from classifier.models import Post
from classifier import choices

def home(req):
	options = {
		'cities': choices.cities(),
		'categories': choices.categories()
	}
	return render(req, 'classifier/home.html', options)


def search(req):
	posts = Post.objects.order_by('-created').filter(is_published=True, status=Post.Status.APPROVED)

	keywords = req.GET.get('q', None)
	if keywords:
		posts = posts.filter(title__icontains=keywords).filter(desc__icontains=keywords)
		#print('>> keywords search:', keywords)

	city = int(req.GET.get('city', 0))
	if city:
		posts = posts.filter(city=city)
		#print('>> city search:', city, type(city))

	category = int(req.GET.get('category', 0))
	if category:
		posts = posts.filter(category=category)
		#print('>> category search:', category)

	paginator = Paginator(posts, 25)
	page = req.GET.get('page', 1)
	page_obj = paginator.get_page(page)

	options = {
		'cities': choices.cities(),
		'categories': choices.categories(),
		'posts': posts,
		'values': req.GET
	}
	return render(req, 'classifier/search.html', options)


def show_post(req, city, category, post_id, title):

	post = get_object_or_404(Post, pk=post_id, is_published=True, status=Post.Status.APPROVED)
	options = {
		'post': post,
		'images': post.get_images()
	}
	return render(req, 'classifier/show_post.html', options)
