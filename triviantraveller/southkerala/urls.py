from django.urls import path
from southkerala import views

app_name = "southkerala"

urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',views.blog,name="blog"),
    path('blogdetail/',views.blogdetail,name="blogdetail"),
    path('comments/',views.comments,name="comments"),
    path('about/',views.about,name="about"),
    path('destinations/',views.destinations,name="destinations"),
    path('tips/',views.tips,name="tips"),
    path('suggesions/',views.suggesions,name="suggesions"),
    #path('enquiry/',views.enquiry,name="enquiry"),
]
