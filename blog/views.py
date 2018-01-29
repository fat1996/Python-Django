# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import Posts, Comments, Subscribers
from django.template import loader

# Create your views here.
def index(request):
	return HttpResponse("<h1>This is the main page.</h1>")

def showPosts(request):
	all_posts = Posts.objects.all()
	context = {
		'all_posts': all_posts
	}
	return render(request, "index.html", context)	

def showPostById(request, post_id):
	try:
		post = Posts.objects.get(id = post_id)
	except Posts.DoesNotExist:
		raise Http404("Post doesn't exist.")
	return render(request, "ShowPostByID.html", {'post': post})

def showComments(request):
	all_comments = Comments.objects.all()
	html = '<h1>This is the list of comments:</h1> <br>'
	for comment in all_comments:
		html += '<b>Comment:</b> ' + comment.comment + '<br>'
	return HttpResponse(html)

def showSubscribers(request):
	all_subscribers = Subscribers.objects.all()
	html = '<h1>This is the list of subscribers:</h1> <br>'
	for subscriber in all_subscribers:
		html += '<b>Subscriber:</b> ' + comment.comment + '<br>'
	return HttpResponse(html)
