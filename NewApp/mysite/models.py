from django.db import models

AGE_CHOICES = (
        ('18','18'),
        ('19','19'),
        ('20','20'),
        ('21','21'),
        ('22','22'),
        ('23','23'),
        ('24','24'),
        ('24~','24~'),
        )

SEX_CHOICES = (
        ('M','男'),
        ('F','女'),
        ('E','その他'),
)

class User(models.Model):
    user_name = models.CharField(max_length=15)
    user_age = models.CharField(max_length=3,choices=AGE_CHOICES,default='18')
    user_sex = models.CharField(max_length=3,choices=SEX_CHOICES,default='M')

class Words(models.Model):
    words = models.CharField(max_length=50,blank=True)
    meaning = models.CharField(max_length=100,blank=True)

class TestImage(models.Model):
    created_image = models.ImageField(upload_to="images/")

class Final_data(models.Model):
    final_images = models.ImageField(upload_to="new_images/",blank=True)
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)

class Karuta_data(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    mistake_count = models.IntegerField(null=True,blank=True)
    finished_time = models.IntegerField(null=True,blank=True)

class Final_Test(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    answer = models.TextField(null=True,blank=True)
