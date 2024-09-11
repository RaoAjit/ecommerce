from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from app.models import product,registration,customer,cart,orderplaced
from app.form import userregi,adressform,loginn
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def home(request):
 products=product.objects.filter(pdtype='mobile')
 ajproduct=product.objects.all()
 ajcart=cart.objects.all()
 count=0
 for x in ajcart:
  count=count+1
  
 for j in products:
  print(j.id)
 return render(request, 'app/home.html',{'products':products,'allpr':ajproduct,'count':count})


class product_detail(View):
 def get(self,request,id):
  pimage=product.objects.get(id=id)
  return render(request, 'app/productdetail.html',{'pimage':pimage})
 

def add_to_cart(request):
  myid=request.GET.get('proid')
  usr=request.user
  ajit=product.objects.get(id=myid)
  annu=product.objects.all()  
  mycart=cart.objects.filter(user=usr)
  for j in mycart:
   if j.product.id == ajit.id:
    print(ajit.id+200)
    j.quantity=j.quantity+1
    j.save()
    return redirect('/show-cart') 
  cart(user=usr,product=ajit).save()
  anu=cart.objects.all()
  return redirect('/show-cart')


def showcart(request):
  anu=cart.objects.filter(user=request.user)
  if anu :
   amount=0
   tamount=0
   for x in anu:
    amount= amount+(x.product.pddsprice*x.quantity)
   tamount=amount+70
   return render(request,'app/addtocart.html',{'annu':anu,'amount':amount,'tamount':tamount})
  else:
   return render(request,'app/empty.html')
  
 


def minus_cart(request):
 if request.method=="GET":
  tr=product.objects.filter(pddsprice=78000.0)
  prod_id=request.GET['prod_id']
  c=cart.objects.get(Q(product=prod_id) & Q(user=request.user)) 
  c.quantity=c.quantity-1
  print(c.quantity)
  c.save()
  an=cart.objects.filter(user=request.user)
  amount=0
  tamount=0
  for j in an:
   amount=amount+(j.product.pddsprice*j.quantity)
   print(amount)
  tamount=amount+70
  data={
   'quantity':c.quantity,
   'amount':amount,
   'tamount':tamount,
   'totalcost':c.totalcost
  }
  return JsonResponse(data)
 
def plus_cart(request):
  if request.method=="GET":
   tr=product.objects.filter(pddsprice=78000.0)
   prod_id=request.GET['prod_id']
   c=cart.objects.get(Q(product=prod_id) & Q(user=request.user)) 
   c.quantity=c.quantity+1
   print(c.quantity)
   c.save()
   an=cart.objects.filter(user=request.user)
   amount=0
   tamount=0
   for j in an:
    amount=amount+(j.product.pddsprice*j.quantity)
    print(amount)
   tamount=amount+70
   data={
   'quantity':c.quantity,
   'amount':amount,
   'tamount':tamount,
   'totalcost':c.totalcost
  }
   return JsonResponse(data)
  
def remove_cart(request):
 print("hii")
 if request.method=="GET":
  tr=product.objects.filter(pddsprice=78000.0)
  prod_id=request.GET['prod_id']
  print(prod_id)
  c=cart.objects.get(Q(product=prod_id) & Q(user=request.user)) 
  c.delete()
  an=cart.objects.filter(user=request.user)
  amount=0
  tamount=0
  for j in an:
   amount=amount+(j.product.pddsprice*j.quantity)
   print(amount)
  tamount=amount+70
  data={
   'amount':amount,
   'tamount':tamount
  }
  return JsonResponse(data)
 
 
def buy_now(request):
 return render(request, 'app/buynow.html')

@method_decorator(login_required, name='dispatch')
class profile(View):
 def get(self,request):
  fm=adressform()
  return render(request, 'app/profile.html',{'form': fm})
 def post(self,request):
  fm=adressform(request.POST)
  if fm.is_valid():
   usr=request.user
   name=fm.cleaned_data['name']
   locality=fm.cleaned_data['locality']
   city=fm.cleaned_data['city']
   zipcode=fm.cleaned_data['zipcode']
   state=fm.cleaned_data['state']
   reg=customer(user=usr,name=name,locality=locality,city=city,zipcode=zipcode,state=state)
   reg.save()
   #messages.success('congrats',request)
   return render(request, 'app/profile.html',{'form': fm})
   
@login_required
def address(request):
 usr=request.user
 cuser=customer.objects.filter(user=usr)
 return render(request, 'app/address.html',{'cuser':cuser})

@login_required
def orders(request):
 op=orderplaced.objects.filter(user=request.user)
 return render(request, 'app/orders.html',{'order_placed':op})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 
  mobile=product.objects.all()
  return render(request, 'app/mobile.html',{'mobile':mobile})

#def logi(request):
 #fm=PasswordChangeForm(request)
 #if request.method =='POST':
   #fm=AuthenticationForm(request=request,data=request.POST)
  #if fm.is_valid():
   #uname=fm.cleaned_data['username']
   #upass=fm.cleaned_data['password']
   #user=authenticate(username=uname,password=upass)
   #if user is not None:
    #login(request,user)
    #return HttpResponseRedirect('/mobile/')
 #return render(request, 'app/login.html',{'forms':fm})

def log_out(request):
 
 if request.user.is_authenticated:  
  logout(request)
  return redirect('/accounts/login')

def customerregistration(request):
  fm=userregi()
  if request.method == 'POST':
   fm=userregi(request.POST)
   if fm.is_valid():
    messages.success(request,'congragulation')
    ajit='i am meawoo'
    fm.save()
    return render(request,'app/customerregistration.html',{'ajj':fm,'ajit':ajit}) 
  return render(request,'app/customerregistration.html',{'ajj':fm})
  #return render(request,'app/customerregistration.html',{'userregi':userregi})

@login_required
def checkout(request):
 usr=request.user
 prdetail=cart.objects.filter(user=usr)
 add=customer.objects.filter(user=usr)
 return render(request, 'app/checkout.html',{'prdetail':prdetail,'add':add})

@login_required
def paymentdone(request):
  if request.user.is_authenticated:
   custid=request.GET.get('custid')
   ccustomer=customer.objects.get(id=custid)
   ccart=cart.objects.filter(user=request.user)
  for z in ccart:
   orderplaced(user=request.user,customer=ccustomer,product=z.product,quantity=z.quantity).save()
   z.delete()
  return redirect('/orders')
   




def form(request):
 try:
  if request.method == 'POST':
   pdtype=request.POST.get('pdtype')
   pdbrand=request.POST.get('pdbrand')
   pddsprice=request.POST.get('pddsprice')
   pddescription=request.POST.get(' pddescription')
   pdprice=request.POST.get('pdprice')
   pdimage=request.POST.get('pdimage')
   product1=product(pdtype=pdtype,pdprice=pdprice,pddsprice=pddsprice,pddescription=pddescription,pdbrand=pdbrand,pdimage=pdimage)
   product1.save()
   return render(request,'form.html')
 except:
  pass
 return render(request,'form.html')

def search(request):
 if request.method == "GET":
  sitem=request.GET.get('jojo')
 
  if sitem=='':
   caution='sorry you have not searched anything '
   return render(request,'app/search.html',{'caution':caution})
   
  if sitem is not None:
   psitem=product.objects.filter(pdbrand__icontains=sitem)
   return render(request,'app/search.html',{'psitem':psitem})
 
