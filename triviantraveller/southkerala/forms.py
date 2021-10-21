from django import forms
#from django.contrib.auth.models import User
from southkerala.models import Blog,Comments,Hotels, Image, Suggesions, Enquiry

class BlogForm(forms.ModelForm):
    post_date = forms.DateField()
    category = forms.CharField()
    title = forms.CharField()
    place = forms.CharField()
    district = forms.CharField()
    details = forms.CharField( widget=forms.Textarea)
    near_railway = forms.CharField()
    near_airport = forms.CharField()
    class Meta():
        model = Blog
        fields = "__all__"

class CommentsForm(forms.ModelForm):
    blog_id = forms.ModelChoiceField(queryset=Blog.objects.all())
    name = forms.CharField()
    email_id = forms.EmailField()
    comment = forms.CharField( widget=forms.Textarea)
    date = forms.DateField()
    class Meta():
        model = Comments
        fields = "__all__"

class HotelsForm(forms.ModelForm):
    blog_id = forms.ModelChoiceField(queryset=Blog.objects.all())
    hotel_name = forms.CharField()
    distance_from_place = forms.CharField()
    details = forms.CharField( widget=forms.Textarea)
    rating = forms.IntegerField()
    images = forms.FileField()
    class Meta():
        model = Hotels
        fields = "__all__"

class ImageForm(forms.ModelForm):
    blog_id = forms.ModelChoiceField(queryset=Blog.objects.all())
    imagepath = forms.FileField()
    class Meta():
        model = Image
        fields = "__all__"

class SuggesionsForm(forms.ModelForm):
    name = forms.CharField()
    suggesion = forms.CharField( widget=forms.Textarea)
    class Meta():
        model = Suggesions
        fields = "__all__"
class EnquiryForm(forms.ModelForm):
    uname = forms.CharField()
    email_id = forms.EmailField()
    enquiry = forms.CharField( widget=forms.Textarea)
    date = forms.DateField()
    class Meta():
        model = Enquiry
        fields = "__all__"
