from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Manufacturer, Product
from django.utils import timezone
# Create your views here.
def index(request):
	manufacturers = Manufacturer.objects.all()
	products = Product.objects.all().select_related('manufacturer')
	context = {
		"manufacturers": manufacturers,
		"products": products,
	}
	return render(request, 'products/index.html', context)

def new_product(request):
	count_errors = 0
	if len(request.POST['name']) < 1:
		messages.error(request, 'Product name cannot be blank!')
		count_errors += 1
	elif len(request.POST['name']) < 8:
		count_errors += 1
		messages.error(request, 'Product name must be at least 8 characters long!')
	else:
		product_name = request.POST['name']

	if request.POST['price'] == '':
		count_errors += 1
		messages.error(request, 'Price cannot be zero!')
	else:
		price = request.POST['price']

	if len(request.POST['description']) >= 50:
		count_errors += 1
		messages.error(request, 'Your description cannot be longer than 50 characters!')
	else:
		description = request.POST['description']

	if count_errors > 0:
		return redirect('/')
	else:
		print "Hello there, you made it past validation!"
		manufacturer = Manufacturer.objects.get(id=int(request.POST['manufacturer']))
		Product.objects.create(name = product_name, price = price, description = description, created_at = timezone.now(), manufacturer = manufacturer)
		return redirect('/')

def details(request, product_id):
	product = Product.objects.get(id=product_id)
	manufacturers = Manufacturer.objects.all()
	context = {
		"product": product,
		"manufacturers": manufacturers,
	}
	return render(request, 'products/product.html', context)

def update(request, product_id):
	count_errors = 0
	if len(request.POST['name']) < 8:
		messages.error(request, 'Your product\'s name must be at least 8 characters!')
		count_errors += 1
	if request.POST['price'] == '' or request.POST['price'] == '0':
		messages.error(request, 'Price must be greater than 0!')
		count_errors += 1
	if len(request.POST['description']) >= 50:
		messages.error(request, 'Description must be less than 50 characters!')
		count_errors += 1

	if count_errors > 0:
		return redirect('/details/%s' % str(product_id))
	else:
		product = Product.objects.get(id=product_id)
		manufacturer = Manufacturer.objects.get(id=request.POST['manufacturer'])
		product.manufacturer = manufacturer
		product.name = request.POST['name']
		product.price = request.POST['price']
		product.description = request.POST['description']
		product.save()
		return redirect('/')

def delete(request, product_id):
	product = Product.objects.get(id = product_id)
	product.delete()
	return redirect('/')
