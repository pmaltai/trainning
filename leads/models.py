from django.db import models
from django.contrib.auth.models import AbstractUser
import misaka
from django.utils.text import slugify

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    slug = models.SlugField(allow_unicode=True, null=True, blank=True)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    images = models.ImageField(upload_to="images/", default="images/default.png")
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return self.first_name

    def save(self, *args,**kwargs):
        self.slug = slugify(self.first_name)
        self.description_html = misaka.html(self.description)
        super(Lead, self).save(*args,**kwargs)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=250)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

