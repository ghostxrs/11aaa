from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    def __str__(self):
        return self.name
class Region(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='image/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.pk)])