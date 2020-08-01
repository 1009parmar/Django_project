from django.shortcuts import render
from django.http import HttpResponse
from .models import product, Contact
from math import ceil

# Create your views here.
def index(request):
    # products = product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nslides,'product':products,'range':range(1,nslides)}
    allProds = []
    catprods = product.objects.values('chatagary','id')
    cats = {item['chatagary'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(chatagary=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nslides),nslides])
    params = {'allProds':allProds}
    return render(request,'shop/index.htm',params)

def about(request):
    return render(request,'shop/about.htm')

def contact(request):
    if request.method == 'POST': 
        name =request.POST.get('name','')
        email =request.POST.get('email','')  
        phone =request.POST.get('phone','')
        desc =request.POST.get('desc','')
        # print(name, email, phone, desc )
        contact = Contact(name=name,email=email,phone=phone,desc=desc) 
        contact.save()
    return render(request,'shop/contact.htm')

def tracker(request):
    return render(request,'shop/tracker.htm')

def search(request):
    return render(request,'shop/search.htm')

def productView(request,myid):
    prod1 = product.objects.filter(id=myid)
    print(prod1)
    return render(request,'shop/productView.htm',{'product' : prod1[0]})
     # Fetch the product using the id  
def checkout(request):
    return render(request,'shop/checkout.htm')

