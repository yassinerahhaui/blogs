from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

def image_name(instance,filename):
    imagename , extension = filename.split('.')
    return "article/%s.%s"%(instance.title,extension)

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_name)
    img_title = models.CharField(max_length=100)
    content = RichTextField()
    description = models.TextField()
    keywords = models.TextField()
    author = models.CharField(max_length=50)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title