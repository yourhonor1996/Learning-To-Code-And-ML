from django.test import TestCase
from blog.models import *
import datetime


class MyTest(TestCase):
    def test_create_author(self):
        author1 = Author.objects.create(name="mohammad")
        # self.assertEqual(Author.objects.get(name="mohammad").name, "mohammad")
        blogpost1 = BlogPost.objects.create(
            title="title1", body="body1", author=author1
        )
        self.assertEqual(blogpost1.author, author1)
        comment1 = Comment.objects.create(blog_post=blogpost1, text="comment text 1")
        blogpost1.copy()
        blogpost1.copy()

        self.assertEqual(BlogPost.objects.all().count(), 3)
        self.assertEqual(Comment.objects.all().count(), 3)
