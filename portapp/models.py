from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =30)
    url= models.URLField(max_length =30)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(max_length = 500,blank =True)
    image_path = models.ImageField(upload_to = 'articles/', null=True,blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    class meta:
        ordering =['name']

