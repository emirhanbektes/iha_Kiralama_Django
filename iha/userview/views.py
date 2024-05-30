from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import status
from django.contrib import messages
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from userview.models import UserProfile
from userview.serializer import userSerializer
from product.models import Product, category
from .forms import UserProfileUpdateForm


@login_required
@api_view(['GET'])
def customer_rent(request):
    user_id = request.user.id
    category_filter = request.GET.get('category', None)
    
    if category_filter:
        user_profiles = UserProfile.objects.filter(user=user_id, product__category=category_filter)
    else:
        user_profiles = UserProfile.objects.filter(user=user_id)
    
    serializer = userSerializer(user_profiles, many=True)
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    context = {
        'product': serializer.data,
        'categories': categories
    }

    return render(request, 'userview/customerRent.html', context)


@api_view(['GET', 'POST'])
def update_rent_date(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)

    if request.method == 'GET':
        form = UserProfileUpdateForm(instance=user_profile)
        return render(request, 'userview/update_Rent.html', {'form': form, 'product': user_profile})
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('customer_rent')  # Güncelleme işlemi başarılıysa ana sayfaya yönlendir
    else:
        return render(request,'userview/update_Rent.html',{'form': form, 'product': user_profile})
    
@api_view(['GET'])
def userRent_list(request):
    
    products = UserProfile.objects.all()
    serializer = userSerializer(products, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def delete_user_profile(request, pk):   
    profile = UserProfile.objects.get(pk=pk)
    profile.delete()    
    return redirect('customer_rent')  # or whatever your desired redirect view is