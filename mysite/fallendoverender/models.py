from django.db import models

# Create your models here.
class profile(models.Model):
	Name = models.CharField(max_length=50)
	Pronouns = models.CharField(max_length=50)
	Bio = models.CharField(max_length=1000)
	Birthday = models.DateField()
	Followers = models.ManyToManyField('self', symmetrical = False, blank = True)
	Profile_pic = models.ImageField("Profile Picture", upload_to = 'profile_pics/')
	def __str__(self):
		return self.Name

class post(models.Model):
	Post_text = models.CharField(max_length=1000)
	Pub_date = models.DateTimeField("Date Published")
	Likes = models.ManyToManyField(profile, related_name = "wholiked", blank = True)
	Posted_by = models.ForeignKey(profile, related_name = "poster", on_delete = models.CASCADE)
	Reblog_post = models.ForeignKey('self', on_delete = models.SET_NULL, null = True, blank = True)
	Media = models.BooleanField
	def __str__(self):
		return self.Posted_by
	
class media(models.Model):
	Medias_post = models.ForeignKey(post, on_delete = models.CASCADE)
	Media= models.FileField("Media",upload_to = 'post_Media/')
	def __str__(self):
		return self.Medias_post
