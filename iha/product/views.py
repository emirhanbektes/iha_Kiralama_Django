from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404, render
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.decorators import api_view
from .models import Product,category
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, CategoryForm, rentUserForm
from .serializer import ProductSerializer


# Burada Veriler listelenir.

@api_view(['GET'])
def updateProduct(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    categories = category.objects.all()
    context = {'products': serializer.data, 'categories': categories}
    return render(request, 'product/updateProduct.html', context)


@login_required
@api_view(['GET'])
def rent(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    categories = category.objects.all()
    context = {'products': serializer.data, 'categories': categories}
    return render(request, 'product/rent.html', context)
 

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('updateProduct')  # Ürünlerin listelendiği sayfanın ismi
    else:
        form = ProductForm()
    return render(request, 'product/product.html', {'form': form})



def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('updateProduct')  # Ürünlerin listelendiği sayfanın ismi
    else:
        form = CategoryForm()
    return render(request, 'product/product.html', {'form': form})

@api_view(['GET', 'POST'])
def update_Product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'product/update_form.html', {'form': form, 'product': product})
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('updateProduct')
        else:
            return render(request, 'product/update_form.html', {'form': form, 'product': product})
        

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer= ProductSerializer(products, many=True)
    return render(request, 'product/updateProduct.html', {'products': serializer.data})


@api_view(['POST'])
def deleteProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')


@login_required
@api_view(['POST', 'GET'])
def rent_product(request):
    if request.method == 'POST':
        form = rentUserForm(request.POST)
        if form.is_valid():            
            form.user = request.POST.get('user')
            form.product = request.POST.get('product')
            form.startdate = request.POST.get('startdate')
            form.stopdate = request.POST.get('stopdate')
            form.save()
            return redirect('rent_product')  # Redirect to success page
        else:
            errors = form.errors
    else:
        form = rentUserForm()
        errors = None

    products = Product.objects.all()
    return render(request, 'product/rent.html', {'form': form, 'products': products, 'errors': errors})
