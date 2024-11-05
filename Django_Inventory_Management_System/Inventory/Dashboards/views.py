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
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboards-products')
    else:
        form = ProductForm(instance=product)

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'dashboards/products_update.html', context)


@login_required
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboards-products')
    context = {
        'product': product
    }
    return render(request, 'dashboards/products_delete.html', context)


@login_required
def orders(request):
    return render (request, 'dashboards/orders.html', {})