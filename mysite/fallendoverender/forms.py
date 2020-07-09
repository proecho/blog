from django import forms

class like(forms.Form):
	Like_This = forms.BooleanField(widget=forms.CheckboxInput)
	
class sign_up_form(forms.Form):
	Name = forms.CharField(label = 'Name', max_length=500)
	Pronouns = forms.CharField(label = 'Pronouns', max_length = 500)
	Bio = forms.CharField(label = 'Bio', max_length = 2000)
	Birthday = forms.DateField(label='Birthday')
	Profile_pic = forms.ImageField(label='Profile_pic')
