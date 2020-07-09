from django.shortcuts import get_object_or_404, render
from .models import profile, post, media
from django.shortcuts import render
from django import forms
from .forms import sign_up_form
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def getrecentposts(profile_id, page_number=0):
	print(page_number)
	return post.objects.filter(Posted_by = profile_id).order_by('pub_date')[(page_number)*10:(page_number+1)*10]

def profile_page(request, profile_id, page_number):
	print(page_number)
	user_profile = get_object_or_404(profile, pk = profile_id)
	ourposts = getrecentposts(profile_id, page_number)
	return render(request,'fallendoverender/profile.html', {'user_profile': user_profile}) 
	
def post_page(request, post_id):
	the_post = get_object_or404(post, pk = post_id)
	return render(request, 'fallendoverender/post.html', {'the_post': the_post})

def home(request):
	return render(request, 'fallendoverender/home.html')

def followers(request, profile_id):
	user_profile = get_object_or_404(profile, pk = profile_id)
	return render(request, 'fallendoverender/follower.html', {'user_profile': user_profile})
	
def signup(request):
	if request.method == 'POST':
		form = sign_up_form(request.POST,request.FILES)
		if form.is_valid():
			data=form.cleaned_data
			NewProfile = profile(**data)
			NewProfile.save()
			return HttpResponseRedirect(reverse('Home'))

		
	else:		 
		return render(request, 'fallendoverender/signup.html')
	
