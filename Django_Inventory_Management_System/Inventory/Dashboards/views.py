from django.shortcuts import render
from django.contrib.auth.decorators import  login_required

@login_required
def index(request):
    return render(request, 'dashboards/index.html', {})

@login_required
def staff(request):
    return render (request, 'dashboards/staff.html', {})

@login_required
def products(request):
    return render (request, 'dashboards/products.html', {})

@login_required
def orders(request):
    return render (request, 'dashboards/orders.html', {})