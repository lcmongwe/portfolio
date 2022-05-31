from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.
class ImagesTest(TestCase):
    '''
    test class for Images model
    '''
    def setUp(self):
       
        self.new_category = Category(name='food')
        self.new_category.save_category()
        self.new_location = Location(name='Nairobi')
        self.new_location.save_location()
        self.new_picture = Image(name='chapati',url='http://photos.example',location=self.new_location, description='local food', image_path='images/food.jpg' )
        self.new_picture.save_image()
        self.picture2 =Image(name='ugali',url='http://photos.example2',location=self.new_location, description='this is ugali', image_path='images/ugali.jpg' )
        self.picture2.save_image()
    def tearDown(self):
     
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()
    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(Image.objects.all()) == 2)
    def test_instances(self):
        '''
         method to test instances created successfully during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,Image))
        self.assertTrue(isinstance(self.new_category, Category))
        self.assertTrue(isinstance(self.new_location, Location))

    def test_delete_image(self):
        '''
        test method to ensure an Image is deleted correctly deleted
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(Image.objects.all()) == 1)


    def test_search_image(self):
    
        image = Image.search_by_category(self.new_picture.category)
        print(image)


    def test_filter_by_location(self):
        image = Image.filter_by_location(self.another_picture.location)
        print(image)

class CategoryTest(TestCase):
    '''
    test class for Category model
    '''
    def setUp(self):
  
        self.new_category = Category(name='category1')
        self.new_category.save_category()

    def tearDown(self):
        '''
        test method to delete Category instance
        '''
        Category.objects.all().delete()

    def test_save_category(self):
        '''
        test for Category instance has been correctly saved
        '''
        self.assertTrue(len(Category.objects.all()) == 1)

    def test_delete_category(self):
        '''
        test a Category instance has been correctly deleted
        '''
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)


class LocationTest(TestCase):
    '''
    test class for Location model
    '''
    def setUp(self):
    
        self.new_location = Location(name='nairobi')
        self.new_location.save_location()

    def test_save_location(self):
        '''
        test  a Location instance has been correctly saved
        '''
        self.assertTrue(len(Location.objects.all()) == 1)

    def test_delete_location(self):
        '''
        test a Location instance has been correctly deleted
        '''
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)


