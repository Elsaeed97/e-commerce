from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product 
from cart.models import Cart
from django.core.paginator import Paginator
# Create your views here.

def products(request):
	products_list = Product.objects.order_by('-date_created')
	paginator = Paginator(products_list,6) #show 6 per page
	page = request.GET.get('page')
	products = paginator.get_page(page)
	context = {
		'products': products,
	}
	return render(request, 'products/product_list.html', context)


def details(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	products = Product.objects.order_by('-date_created')[:4]
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	context = {
		'product': product,
		'products' : products ,
		'cart' : cart_obj
	}

	return render(request,'products/product_detail.html',context)