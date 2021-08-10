from django.shortcuts import render,redirect
from .forms import ProductForm,Category_Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.

@login_required
def products(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST or None, request.FILES or None)
        if product_form.is_valid():
            f = product_form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Product Added Successfully..')
            return redirect('Home:home')
        else:
            messages.error(request, 'failed to add Product')
    else:
        product_form = ProductForm()
    template = 'Products/products.html'
    return render(request, template, {'product_form': product_form})


def category(request):
    template = 'Products/category_form.html'
    if request.method == 'POST':
        category_form = Category_Form(request.POST or None)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,'Category is added')
            return redirect('Home:home')
        else:
            messages.error(request,'Please correct error below')
    else:
        category_form = Category_Form()
    return render(request,template,{'category_form':category_form})


def product_list(request):
    products = Product.objects.all()
    return render(request,'Products/shop.html',{'products':products})

def singleproduct(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'Products/singleproduct.html',{'product':product})


def my_products(request):
    template = 'Products/my_products.html'
    products = Product.objects.filter(user__id=request.user.id)
    return render(request,template,{'products':products})


def update_products(request,pk):
    template = 'Products/products.html'
    product = Product.objects.get(pk=pk)
    pf = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if pf.is_valid():
        pf.save()
        messages.success(request,'product updated successfully')
    else:
        pf = ProductForm(instance=product)
        messages.error(request,'please correct the error below')
    return render(request,template,{'product_form':pf})


