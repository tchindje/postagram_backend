from django.db import models
from core.abstract.models import AbstractModel, AbstractManager


class CommentManager(AbstractManager):
    pass


class Comment(AbstractModel):
    post = models.ForeignKey(to="core_post.Post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE, related_name="comments")

    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.author.name
