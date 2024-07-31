
from django.db import models

class UserProfile_models(models.Model):
    user_id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=150,null=False)
    user_password = models.CharField(max_length=128,null=False)  
    user_email = models.EmailField(unique=True,null=False)
    user_birthday = models.DateField(null=True, blank=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    addr = models.CharField(max_length=255, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class ZipCode(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10, unique=True)  

    def __str__(self):
        return f"{self.zip_code} - {self.city}, {self.district}"
    
class User_Follower(models.Model):
    user_id = models.IntegerField(null=False)
    user_name = models.CharField(max_length=200)
    user_follow_id = models.IntegerField(null=False)
    user_follow_name = models.CharField(null=False,max_length=200)
    follow_start_date = models.DateField(auto_now_add=True,null=False)
    cancel_follow = models.BooleanField(default=False)
    cancel_follow_date = models.DateField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.user_name} is been followed by {self.user_follow_name}"

    class Meta:
        db_table = 'User_follow_table'

class User_Follow_Post(models.Model):
    post_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    user_name = models.CharField(max_length=200)
    like_post = models.BooleanField(default=True)
    like_post_start_date = models.DateField(auto_now_add=True,null=False)
    cancel_start_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.post_id
    
    class Meta:
        db_table = 'User_Follow_Post'
        