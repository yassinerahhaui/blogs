from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
def image_upload(instance,filename):
    imagename , extension = filename.split('.')
    return "service/%s.%s"%(instance.title,extension)


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload)
    img_title = models.CharField(max_length=100)
    content = RichTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return self.title