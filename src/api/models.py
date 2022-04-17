from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments",null=True)
    username = models.CharField(max_length=200)
    text = models.TextField()
    answer_to = models.ForeignKey("self", on_delete=models.CASCADE, related_name='answers', null=True)
