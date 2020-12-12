from django.db import models

# Create your models here.
class Book(models.Model):
  
    title = models.CharField(max_length = 36, blank=False, unique=True)
    description = models.TextField(max_length = 256, blank=True, default=None)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    createdtime = models.DateTimeField(auto_now=True)
    published = models.DateField(blank = True, null=True)
    is_published=models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank = True)
