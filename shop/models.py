from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=200,default = None)
    price =models.IntegerField(blank=True ,null= True)
    content = models.TextField(default = None)
    image = models.ImageField(default = 'default.jpg',upload_to="media/images")

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    user =models.ForeignKey(User, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete =models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class Order(models.Model):
    user =models.ForeignKey(User, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date =models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()


    def __str__(self):
        return self.user.username
