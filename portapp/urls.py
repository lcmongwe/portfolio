from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
path('', views.home, name="home"),
path('big_image/<image_id>', views.big_image, name="big_image"),
path('search_category', views.search_category, name="search_category"),
 path('delete_image/<image_id>', views.delete_image, name="delete_image"),
 path('locations/<location>', views.location, name="location"),
path('categories/<category>', views.category, name="category"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
