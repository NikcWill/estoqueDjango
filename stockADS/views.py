from django.shortcuts import render, HttpResponse, redirect
from.models import Products, Categories
from random import randint
from datetime import datetime
from django.contrib.auth.decorators import login_required
 
@login_required(redirect_field_name='login')
def index(request):

  #return HttpResponse('Estou no Django')
  #from Product select *

  #produtos = Products.objects.all()
  produtos = Products.objects.filter( user_id=request.user.id, in_stock=True)
  #for produto in produtos:
    #print(f'{produto.name} + {produto.price}')
  return render(request, 'pages/index.html', {'produtos':produtos})
  
def search_product(request):
  q = request.GET.get('q')
  produtos = Products.objects.filter(name__icontains=q, cod__startswith=q, in_stock=True)
  return render(request, 'pages/index.html', {'produtos':produtos})
  

def product_detail(request, id):
  product = Products.objects.get(id=id)
  return render(request, 'pages/product_detail.html', {'product': product})

def sell_product(request, id):
  product = Products.objects.get(id=id)
  if product.qtd > 0:
    product.qtd -= 1
    product.save()
    
    if product.qtd <= 0:
      product.in_stock = False
      product.save()
      return redirect('home')
    
  return redirect('product-detail', id)

def delete_product(request, id):
  product = Products.objects.get(id=id)
  product.delete()
  return redirect('home')

def add_product(request, ):
  if request.method == 'POST':

    name = request.POST.get('name')
    cod = randint(100, 10000)
    category = request.POST.get('category')
    picture = request.FILES.get('picture')
    price = request.POST.get('price')
    description = request.POST.get('description')
    qtd = request.POST.get('qtd')
    discount = request.POST.get('discount')
    created_at = datetime.now()
    in_stock = True

    Products.objects.create(
      user_id=request.user.id,
      name=name, cod=cod, category_id=category, picture=picture,
      price=price, description=description, qtd=qtd, discount=discount,
      created_at=created_at, in_stock=in_stock
    )
    return redirect('home')

  else:
    categories = Categories.objects.all()
    return render(request, 'pages/add-product.html',{'categories':categories})