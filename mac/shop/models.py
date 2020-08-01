from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    chatagary = models.CharField(max_length=50,default="")
    subchatagary = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300,default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name  

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    phone = models.IntegerField(max_length=10,default=0)
    desc = models.CharField(max_length=500,default="")


    def __str__(self):
        return self.name
