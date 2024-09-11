from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import product,customer,cart,orderplaced,registration

class adproduct(admin.ModelAdmin):
    list_display=['pdtype','pdprice','pddsprice','pddescription','pdbrand','pdimage']
admin.site.register(product,adproduct)

# Register your models here.
class adcustomer(admin.ModelAdmin):
    list_display=['user','name','locality','city','zipcode','state']
admin.site.register(customer,adcustomer)

class adcart(admin.ModelAdmin):
    list_display=['user','product','quantity']
admin.site.register(cart,adcart)

class adorderplaced(admin.ModelAdmin):
    list_display=['user','customer','product','quantity','order_date','status']
admin.site.register(orderplaced,adorderplaced)


class adregistration(admin.ModelAdmin):
    list_display=['email','password','password2']
admin.site.register(registration,adregistration)
