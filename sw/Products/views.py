from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm,Category_Form,Rating_Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product,Ratings
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
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
            return redirect('Products:my_products')
        else:
            messages.error(request, 'failed to add Product')
    else:
        product_form = ProductForm()
    template = 'Products/products.html'
    return render(request, template, {'product_form': product_form})

@login_required
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
    ratings = Ratings.objects.filter(product__id=pk)
    return render(request,'Products/singleproduct.html',{'product':product,'ratings':ratings})

#
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


def delete_product(request,pk):
    template = 'Products/delete_product.html'
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Products:my_products')
    return render(request,template)


@login_required
def ratings(request,pk):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = Rating_Form(request.POST)
        if form.is_valid():
            data = Ratings()
            data.subject = request.POST['subject']
            data.comment = request.POST['comment']
            data.rate = request.POST['rate']
            data.product_id = pk
            usr = request.user
            data.user_id = usr.id
            data.save()
            messages.success(request,'Your Review submitted successfully')
            return HttpResponseRedirect(url)
    else:
        return redirect('account_login')



# def search(request):
#     if request.method == 'GET':
#         srh = request.GET['search']
#         products = Product.objects.filter(name__contains=srh)
#         return render(request,'Products/shop.html',{'products':products})

def search(request):
    template = 'Products/shop.html'
    if request.method=='GET':
        name = request.GET["name"]
        # cat = request.GET["category"]
        price = request.GET["price"]
        print(price)

        # prd = Product.objects.filter(name__contains=srh)  # search by product name
        # prd = Product.objects.filter(Q(name__contains=name) | Q(category__name__contains=cat))
        # print(prd)
        prd = Product.objects.filter(Q(name__contains=name) & Q(price__lt=price)) # search by product name and and price less than use two search field in html
        return render(request,template,{'products':prd})
    else:
        return render(request,'Products/shop.html')



def winter(request):
    products = Product.objects.filter(category__name='Winter')
    return render(request, 'Products/shop.html', {'products': products})

def summer(request):
    products = Product.objects.filter(category__name='Summer')
    return render(request, 'Products/shop.html', {'products': products})

def Male(request):
    products = Product.objects.filter(gender='M')
    return render(request, 'Products/shop.html', {'products': products})

def Female(request):
    products = Product.objects.filter(gender='F')
    return render(request, 'Products/shop.html', {'products': products})

