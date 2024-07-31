
from django.db import models
from .user_models import UserProfile_models

class PostModels(models.Model):
    post_id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=150,null=False)
    user = models.ForeignKey(UserProfile_models,on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200,null=False)
    post_content = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True,null=False)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.post_title

class PostModels_Comment(models.Model):
    comment_id = models.AutoField(primary_key=True,null=False)
    user_name = models.CharField(max_length=150,null=False)
    user = models.ForeignKey(UserProfile_models,on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    post = models.ForeignKey(PostModels,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True,null=False)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment_id
    
    class Meta:
        db_table = 'post_comment'
