from django.db import models

from user.models import UserModel

# Create your models here.
class PostModel(models.Model):
    content = models.TextField(max_length=1000, verbose_name="Content")
    picture = models.ImageField(upload_to="posts_imgs/", verbose_name="Post picture/image")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication date")
    posted_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-pub_date"]


class PostCommentsModel(models.Model):
    comment = models.CharField(max_length=600, verbose_name="Comment")
    picture = models.ImageField(upload_to="comments_imgs/", verbose_name="Comment picture/image")
    comm_date = models.DateTimeField(auto_now_add=True, verbose_name="Commented on")
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["-comm_date"]


