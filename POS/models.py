
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django_countries.fields import CountryField
from django.core.validators import MinLengthValidator, int_list_validator



# Create your models here.
class Category(models.Model):
    Name= models.CharField(max_length=20)
    IsActive=models.BooleanField()
    def __str__(self):
        return self.Name

def get_user_name():
    return ""
    
def image_upload(instance,filename):
    name,ext=filename.split(".")
    return "items/%s.%s"%(instance.id,ext)
class Item(models.Model):
    Author=models.ForeignKey(User,null=True,on_delete=models.CASCADE,editable=False)
    Name=models.CharField(max_length=20)
    Price=models.FloatField()
    Quantity=models.IntegerField()
    Category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to=image_upload)
    def __str__(self):
        return self.Name
    
    
   
class ItemOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    is_ordered=models.BooleanField(default=False)
    def __str__(self):
        return str(self.item)

    def total_item_price(self):
        return self.item.Price*self.quantity


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(ItemOrder, blank=True)
    order_date=models.DateTimeField(blank=True,null=True)
    is_ordered=models.BooleanField(default=False)
    
    def total_price(self):
        total=0
        for item in self.items.all():
            total+=item.total_item_price()
        return total

class Customer(models.Model):
    Gender = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    Name=models.CharField(max_length=20)
    PhoneNumber=models.IntegerField()
    Address=models.CharField(max_length=70)
    Description=models.TextField(max_length=150,null=True,blank=True)
    Gender = models.CharField(max_length=2, choices=Gender)
    def __str__(self):
        return self.Name


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    phone_no = models.CharField(verbose_name="Phone number", max_length=11,
    validators=[int_list_validator(sep=''),MinLengthValidator(11),])
    area_name=models.CharField(max_length=50)
    street_name = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    additional_directions=models.TextField(null=True,blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username