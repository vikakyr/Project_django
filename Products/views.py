from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import Products, Category, Level
from .forms import CombinedForm
import json
from Products.models import ReservedProduct  



def index(request):
    

    return HttpResponse(Products.objects.all())

def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.name)

def product(request, id):
    product_user = Products.objects.get(pk=id)
    string = "<h1>" + str(product_user) + "</h1>" + "<p> " + str(product_user.price) +  "</p> " + "<p> " + str(product_user.description) +  "</p> "
    return HttpResponse(string)


from .models import Products
from .forms import CombinedForm

from django.shortcuts import render
from .models import Products, Category, Level
from .forms import CombinedForm

from django.shortcuts import render
from .models import Products, Category, Level
from .forms import CombinedForm, ProductDetailsForm





from django.shortcuts import redirect

def home(request):
    grouped_products = {}  
    selected_products = [] 
    selected_options = None
    selected_options_level = None
    product_details_form = None 

    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            selected_options = form.cleaned_data['options']
            selected_options_level = form.cleaned_data['options_level']

            
            category_ids = Category.objects.filter(name__in=selected_options).values_list('id', flat=True)
            level_ids = Level.objects.filter(name=selected_options_level).values_list('id', flat=True)
            filtered_products = Products.objects.filter(category__id__in=category_ids, level__id__in=level_ids)

            
            if form.is_valid():
                product_details_form = ProductDetailsForm()

            
            for product in filtered_products:
                category_name = product.category.name if product.category else 'Other'
                if category_name not in grouped_products:
                    grouped_products[category_name] = []
                grouped_products[category_name].append(product)

                
                chosen_product_id = request.POST.get('chosen_product')
                if chosen_product_id and str(product.id) == chosen_product_id:
                    selected_products.append(product.id)

    else:
        form = CombinedForm()

    return render(request, 'home.html', {'form': form, 'grouped_products': grouped_products, 'selected_options': selected_options, 'selected_options_level': selected_options_level, 'product_details_form': product_details_form, 'selected_products': selected_products})

def add_to_cart(request):
    if request.method == 'POST':
        selected_products = request.POST.getlist('selected_products')
        
        return redirect('add_to_cart')  

    return redirect('home')

'''def cart(request):
    if request.method == 'GET':
        selectedProducts = request.GET.getlist('selectedProductsList')
    print(f'{selectedProducts}')
    context = {'selectedProducts': selectedProducts}
    return render(request, 'cart.html', context)'''



def cart(request):
    if request.method == 'GET':
        selectedProductsJson = request.GET.get('selectedProducts')
        selectedProducts = json.loads(selectedProductsJson) if selectedProductsJson else []

    context = {'selectedProducts': selectedProducts}
    return render(request, 'cart.html', context)

def reserved(request):
    reservedProducts = ReservedProduct.objects.filter(user=request.user).all()
    context = {'reservedProducts': reservedProducts}
    return render(request, 'reserved.html', context)


# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ReservedProductForm

@csrf_exempt
def save_reserved_product(request):
    reservedProductsJson = request.POST.get('reservedProducts')
    reservedProducts = json.loads(reservedProductsJson) if reservedProductsJson else []
    for product in reservedProducts:
        p = Products.objects.get(pk=product["productId"])
        reservedProduct = ReservedProduct(
            user=request.user,
            product=p,
            date=product["date"],
            price=product["price"],
            selected_size=product["selectedSize"])
        reservedProduct.category = p.category
        reservedProduct.save()
    return redirect("reserved")






