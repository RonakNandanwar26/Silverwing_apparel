from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import os

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return ext

def upload_product_image_path(instance, filename):
    new_filename = instance.name
    ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Products/{final_filename}".format(final_filename=final_filename)

def upload_product_video_path(instance, filename):
    new_filename = instance.name
    ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Products/video/{final_filename}".format(final_filename=final_filename)

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=50)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=0)
    availability = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    image1 = models.ImageField(default='default.jpg', upload_to=upload_product_image_path)
    image2 = models.ImageField(default='default.jpg',upload_to=upload_product_image_path, null=True, blank=True)
    image3 = models.ImageField(default='default.jpg',upload_to=upload_product_image_path, null=True, blank=True)
    image4 = models.ImageField(default='default.jpg',upload_to=upload_product_image_path, null=True, blank=True)
    video1 = models.FileField(default='default.mp4', upload_to=upload_product_video_path, null=True, blank=True)

    def __str__(self):
        return self.name


class Ratings(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50,blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " " + self.product.name