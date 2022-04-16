from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)


class Comment(BaseModel):
    username = models.CharField(max_length=200)
    text = models.TextField()
    answer_to = models.ForeignKey("self", on_delete=models.CASCADE, related_name='answers')
