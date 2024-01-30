from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742461 Mai Tokairin views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html',context = context_data)

def homepage_view(request):
    return HttpResponse("Homepage")

def category_view(request):
    return HttpResponse("Category")

def product_view(request):
    return HttpResponse("Product")

def checkout_view(request):
    return HttpResponse("Checkout")

def contact_page(request):
    return HttpResponse("Contact")
