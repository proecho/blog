from django.urls import path

from . import views

urlpatterns = [
	path('',views.home, name='Home'),
	path('<str:profile_id>/<int:page_number>/', views.profile_page, name='profile_page1'),
	path('followers/<str:Profile_id>/', views.followers, name = 'followers'),
	path('signup/', views.signup, name = 'signup'),
	path('post/<str:Post_id>/', views.post_page, name = 'post_page1'),
]
