from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOISES = (
        ('published', 'Опубликован'),
        ('draft', 'Черновик')
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=15, choices=STATUS_CHOISES)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title