from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image= Image(name = 'dress', url = 'https://dress', location = 'nairobi', category = 'general', description ='ver good',image_path = 'dress',)
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

     # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()