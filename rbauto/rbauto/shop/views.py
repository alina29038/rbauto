from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as auth_logout, login
from .services.CatalogService import CatalogService
from .services.OrderService import OrderService

# Create your views here.
def index(request):
    context = CatalogService.getCategories()
    return render(request, 'shop/index.html', context)

def searchDealers(request):
    context = CatalogService.getCategories()
    return render(request, 'shop/partners/search-dealers.html', context)

def catalog(request):
    context = CatalogService.getCategories()
    return render(request, 'shop/catalog/catalog.html', context)

def catalogCategory(request, category_id):
    context = CatalogService.getCategories()
    category = CatalogService.getCategory(category_id)
    context["category"] = category
    context["manufacturers"] = CatalogService.getManufacturers()

    page = request.GET.get('page', 1)
    try:
        page = int(page)
        page = 1 if page < 1 else page
    except:
        page = 1

    page_count = 5

    subcategory = request.GET.get('subcategory', None)
    manufacturer = request.GET.get('manufacturer', None)

    filter_result = CatalogService.getFilteredProducts(category, subcategory, manufacturer)
    context["subcategory"] = filter_result["subcategory"]
    context["manufacturer"] = filter_result["manufacturer"]
    
    paginator = Paginator(filter_result["products"], page_count)
    context["page_obj"] = paginator.get_page(page)
    
    return render(request, 'shop/catalog/category.html', context)

def catalogProduct(request, product_id):
    context = CatalogService.getCategories()
    product = CatalogService.getProduct(product_id)
    context["product"] = product

    return render(request, 'shop/catalog/product.html', context)

def catalogProductOrder(request, product_id):
    if request.method == "POST":
        data = request.POST
        user = None
        if request.user.is_authenticated:
            user = request.user
        OrderService.createOrder(data, product_id, user)

    request.session["previous_url"] = data.get("previous_url", '/')
    return redirect('order-success')

def orderSuccess(request):
    context = CatalogService.getCategories()
    context["previous_url"] = request.session.get("previous_url", '/')
    return render(request, 'shop/orders/order_success.html', context)

def signIn(request):
    context = CatalogService.getCategories()
    if request.user.is_authenticated:
        return redirect('orders')
    if request.method == "POST":
        name = request.POST.get("username", None)
        if not name:
            return render(request, 'shop/auth/sign_in.html', context)
        password = request.POST.get("password", None)
        if not password:
            return render(request, 'shop/auth/sign_in.html', context)
        
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect("orders")
        else:
            return render(request, 'shop/auth/sign_in.html')
    return render(request, 'shop/auth/sign_in.html', context)

def signOn(request):
    context = CatalogService.getCategories()
    if request.user.is_authenticated:
        return redirect('orders')
    if request.method == "POST":
        name = request.POST.get("username", None)
        if not name:
            return render(request, 'shop/auth/sign_on.html', context)
        email = request.POST.get("email", None)
        if not email:
            return render(request, 'shop/auth/sign_on.html', context)
        password = request.POST.get("password", None)
        if not password:
            return render(request, 'shop/auth/sign_on.html', context)
        user = User.objects.create_user(username=name,password=password, email=email)
        user.save()
        return redirect('sign-in')
    return render(request, 'shop/auth/sign_on.html', context)

def logout(request):
    auth_logout(request)
    return redirect('index')

def ordersList(request):
    context = CatalogService.getCategories()
    if request.user.is_authenticated:
        context["orders"] = OrderService.getUserOrders(request.user)
        return render(request, 'shop/orders/orders_list.html', context)
    return redirect('sign-in')
    