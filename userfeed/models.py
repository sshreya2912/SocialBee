from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="images")
    caption=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.caption
class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dp=models.ImageField(upload_to="images")
    bio=models.CharField(max_length=200)
    followers=models.IntegerField(default=0)
    following=models.IntegerField(default=0)
    def __str__(self):
        return self.bio
class Comment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment_text=models.TextField()
    user_comment=models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return self.comment_text
class Like(models.Model):
    user = models.ManyToManyField(User, related_name="likingUser")
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    # for liking post
    @classmethod
    def like(cls, post, liking_user):
        obj, create  = cls.objects.get_or_create(post = post)
        obj.user.add(liking_user)

    # for disliking post
    @classmethod
    def dislike(cls, post, disliking_user):
        obj, create  = cls.objects.get_or_create(post = post)
        obj.user.remove(disliking_user)

    def __str__(self):
        return str(self.post)
    
        
    
#     srno=models.AutoField(primary_key=True)
#     post=models.OneToOneField("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
#     user=models.ManyToManyField()
#     comment=models.TextField()
#     parent=models.BooleanField()
#     timestamp=models.TimeField(auto_now_add=True)
    

