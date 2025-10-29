from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Supplement', 'Supplement'),
        ('Equipment', 'Equipment'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)



    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    # Address Info
    address1 = models.CharField("Address Line 1", max_length=255)
    address2 = models.CharField("Address Line 2", max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField("State/Province", max_length=100)
    zip_code = models.CharField("ZIP/Postal Code", max_length=20)
    country = models.CharField(max_length=100)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"



class Checkout(models.Model):
    # Contact Information
    user = models.ForeignKey( User,on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True,null=True )
    
    # Shipping Address
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    # Order Details (you might want to connect this to an Order model)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # is_completed = models.BooleanField(default=False)
    
    # Payment Information (you might want to store this separately for security)
    # payment_method = models.CharField(max_length=50, blank=True, null=True)
    # payment_status = models.CharField(max_length=50, default='pending')
