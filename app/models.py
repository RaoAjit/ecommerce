from django.db import models
from django.contrib.auth.models import User

#Create your models here.
type=(
    ('mobile','mobile'),
    ('laptop','laptop'),
    ('upper','upper'),
    ('lower','lower')
    )
state=(
    ('odisha','odisha'),
    ('telengana','telengana'),
    ('mp','mp'),
    ('up','up')
    )
status_ch=(
    ('orderd','orderd'),
    ('pending','pending'),
    ('delivered','delivered'),
    ('cancel','cancel'),
    ('packed','packed')
    )
class product(models.Model):
    pdtype=models.CharField(choices=type,max_length=9)
    pdprice=models.FloatField()
    pddsprice=models.FloatField()
    pddescription=models.CharField(max_length=100)
    pdbrand=models.CharField(max_length=100)
    pdimage=models.ImageField(upload_to='myimage')
    def __str__(self):
     return str(self.pdbrand)


class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.TextField(max_length=100)
    locality=models.TextField(max_length=100)
    city=models.TextField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=state,max_length=10)
    def __str__(self):
     return str(self.id)
    
class cart(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   product=models.ForeignKey(product,on_delete=models.CASCADE)
   quantity=models.PositiveIntegerField(default=1)
   def __str__(self):
     return str(self.id)
   @property
   def totalcost(self):
      return self.quantity*self.product.pddsprice
   
class orderplaced(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   customer=models.ForeignKey(customer,on_delete=models.CASCADE)
   product=models.ForeignKey(product,on_delete=models.CASCADE)
   quantity=models.PositiveIntegerField(default=1)
   order_date=models.DateTimeField(auto_now_add=True)
   status=models.CharField(max_length=40,choices=status_ch,default='pending')
   def __str__(self):
     return str(self.id)
   @property
   def totalcost(self):
      return self.quantity*self.product.pddsprice
   

class registration(models.Model):
   email=models.EmailField(max_length=100)
   password=models.CharField(max_length=100)
   password2=models.CharField(max_length=100,null=True)
   def __str__(self):
       return str(self.id)



    

 