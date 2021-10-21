from django.db import models

# Create your models here.


class Blog(models.Model):
    CATEGORY_CHOICE = (
        ('beach','BEACH'),
        ('culture and heritage', 'CULTURE AND HERITAGE'),
        ('hill stations','HILL STATIONS'),
        ('museum','MUSEUM'),
        ('temples','TEMPLES'),
    )
    blog_id = models.AutoField(primary_key=True)#auto increment
    post_date = models.DateField()
    category = models.CharField(max_length=22, choices=CATEGORY_CHOICE, default='beach')
    title = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    details = models.TextField()
    near_railway = models.CharField(max_length=250)
    near_airport = models.CharField(max_length=250)
    def __str__(self):
        return str(self.blog_id)

class Comments(models.Model):
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    com_id = models.AutoField(primary_key=True)#auto increment
    name = models.CharField(max_length=250)
    email_id = models.EmailField(max_length=250)
    comment = models.TextField()
    date = models.DateField()
    def __str__(self):
        return str(self.com_id)

class Hotels(models.Model):
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=250)
    distance_from_place = models.CharField(max_length=250)
    details = models.TextField()
    rating = models.IntegerField()
    images = models.FileField(upload_to='uploads/')
    #order_id = models.CharField(max_length=250)
    def __str__(self):
        return str(self.hotel_id)

class Image(models.Model):
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    image_id = models.AutoField(primary_key=True)
    imagepath = models.FileField(upload_to='uploads/')
    #order_id = models.CharField(max_length=250)
    def __str__(self):
        return str(self.image_id)

class Suggesions(models.Model):
    sugg_id = models.AutoField(primary_key=True)#auto increment
    name = models.CharField(max_length=250)
    suggesion = models.TextField()
    def __str__(self):
        return str(self.sugg_id)

class Enquiry(models.Model):
    enq_id = models.AutoField(primary_key=True)#auto increment
    uname = models.CharField(max_length=250)
    email_id = models.EmailField(max_length=250)
    enquiry = models.TextField()
    date = models.DateField()
    def __str__(self):
        return str(self.enq_id)
