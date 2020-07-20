from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from . import models
from .decorators import unauthenticated_user, allowed_users
from .forms import ProductForm, OrderForm
# Create your views here.


categories = models.Category.objects.all()
context = {'categories': categories}


def main_view(request):
    promoted_products = models.Product.objects.filter(promoted=True)
    main_context = {
        **context,
        'results': promoted_products,
    }
    return render(request, 'mjstore_main/main.html', main_context)


@login_required
def cart_view(request):
    orders = models.Order.objects.filter(user=request.user, status=models.Order.IN_ORDER)
    history_orders = models.Order.objects.filter(Q(user=request.user) & ~Q(status=models.Order.IN_ORDER)).order_by('status')
    cart_context = {
        **context,
        'orders': orders,
        'history_orders': history_orders,
    }

    return render(request, 'mjstore_main/cart.html', cart_context)


def search_view(request):
    if request.method == "POST":
        query = Q()
        search_text = request.POST['search']
        query.add(('name__icontains', search_text), 'AND')
        search_descriptions = request.POST.get('search_description', False)

        if search_descriptions:
            query.add(('description__icontains', search_text), 'OR')

        category = request.POST.get('categories', None)
        if category is not None:
            query.add(('category', models.Category.objects.get(name=category)), 'AND')
   
        results = models.Product.objects.filter(query)

    search_context = {
        **context,
        'results': results,
    }
    return render(request, 'mjstore_main/search_results.html', search_context)


def category_view(request, category):
    category = get_object_or_404(models.Category, name=category)
    products = category.product_set.all()
    category_context = {
        **context,
        'results': products, 
    }
    return render(request, 'mjstore_main/category_detail.html', category_context)


def item_detail_view(request, category, slug):
    product = get_object_or_404(models.Product, slug=slug)
    product_context = {
        **context,
        'product': product, 
    }
    return render(request, 'mjstore_main/product_detail.html', product_context)


@login_required
@allowed_users(allowed_roles=['staff'])
def add_product_view(request):
    product_context = {
        'product_form': ProductForm
    }
    if request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'mjstore_main/add_product.html', product_context)


@login_required
def add_to_cart_view(request, product_name):
    product = models.Product.objects.get(name=product_name)
    product_quantity = product.quantity
    if product_quantity < 1:
        return HttpResponseRedirect('/')
    product.quantity = product.quantity - 1
    product.save()
    latest_order_number = models.Order.objects.latest('order')
    order_number = int(latest_order_number.order) + 1
    order = models.Order(order=order_number, user=request.user, product=product)
    order.save()
    return HttpResponseRedirect('/cart')


@login_required
def delete_order_view(request, order_id):
    order = models.Order.objects.get(order=order_id)
    order.status = models.Order.CANCELLED
    quantity = order.product.quantity
    order.product.quantity = quantity + 1
    order.save()
    order.product.save()
    return HttpResponseRedirect('/cart')


@login_required
@allowed_users(allowed_roles=['staff'])
def manage_orders_view(request):
    orders = models.Order.objects.all().order_by('status')
    for order in orders:
        order.form = OrderForm(instance=order)
    
    orders_context = {
        **context,
        'orders': orders,

    }
    return render(request, 'mjstore_main/manage_orders.html', orders_context)


@login_required
@allowed_users(allowed_roles=['staff'])
def update_order_view(request, order_id):
    if request.method == 'POST':
        order = models.Order.objects.get(order=order_id)
        order.status = request.POST['status']
        order.save()
    return HttpResponseRedirect('/manage-orders')
