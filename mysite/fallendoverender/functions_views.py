from models import post

def getrecentposts(profile_id, page_number=0):
	print(page_number)
	return post.objects.filter(Posted_by = profile_id).order_by('pub_date')[(page_number)*10:(page_number+1)*10]
