from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.caption)

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(db_index=True, unique=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=SET_NULL, null=True)

    def __str__(self):
        return '{}  ({})'.format(self.user_name, self.text)