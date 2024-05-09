from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=100)
    metaDescription = models.TextField(null=True, blank=True)
    postedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title