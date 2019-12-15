from django.shortcuts import render
from products.models import Product 
# Create your views here.

def index(request):
	products = Product.objects.order_by('-date_created')[:8]
	bestseller = Product.objects.order_by('-date_created').filter(bestseller=True)[:4]
	featured = Product.objects.order_by('-date_created').filter(featured=True)[:3]
	context = {
		'products':products,
		'bestsellers': bestseller,
		'featured_products' :  featured,
	}
	return render(request,'pages/index.html', context)