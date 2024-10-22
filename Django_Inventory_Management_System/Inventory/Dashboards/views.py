from django.shortcuts import render

def index(request):
    return render(request, 'dashboards/index.html', {})

def staff(request):
    return render (request, 'dashboards/staff.html', {})

def products(request):
    return render (request, 'dashboards/products.html', {})

def orders(request):
    return render (request, 'dashboards/orders.html', {})