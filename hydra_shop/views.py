from django.shortcuts import render, get_object_or_404

from hydra_shop.models import Category, Product, ProductImage


def index(request):
    return render(request, 'index.html')


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def products_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products.html', {'category': category, 'products': products})


def product_info(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = ProductImage.objects.filter(product=product)
    return render(request, 'product_info.html', {'product': product, 'images': images})
