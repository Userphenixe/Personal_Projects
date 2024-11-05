from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required
from .models  import Product
from .forms import  ProductForm


@login_required
def index(request):
    return render(request, 'dashboards/index.html', {})

@login_required
def staff(request):
    return render (request, 'dashboards/staff.html', {})

@login_required
def products(request):
    products = Product.objects.all()
    if  request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboards-products')
    else:
        form  = ProductForm()
    context = {
        'products': products,
        'form':  form,
    }
    return render (request, 'dashboards/products.html',  context)


@login_required
def orders(request):
    return render (request, 'dashboards/orders.html', {})