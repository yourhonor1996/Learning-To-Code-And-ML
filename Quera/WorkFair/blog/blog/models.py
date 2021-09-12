from django.db import models
from django.utils import timezone
from copy import deepcopy

# TODO write all of your code here...
class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        blog_post_clone = BlogPost.objects.get(id=self.id)
        comments = self.comment_set.all()
        blog_post_clone.id = None
        blog_post_clone.save()
        blog_post_clone.date_created = timezone.now()
        blog_post_clone.save()
        for comment in comments:
            comment_clone = deepcopy(comment)
            comment_clone.id = None
            comment_clone.save()
            comment_clone.blog_post = blog_post_clone
            comment_clone.save()
        return blog_post_clone.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
