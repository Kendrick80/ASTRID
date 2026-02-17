from django.db import models
import uuid
from .utils import users_listings_path

class Blog(models.Model):
    title = models.CharField(max_length=500, default=None)  # Changed 'Title' to 'title'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=500, default=None)  # Changed 'Author' to 'author'
    blog = models.TextField()  # Changed 'Blog' to 'blog'
    image = models.ImageField(upload_to=users_listings_path)

    def __str__(self):
        return self.title
