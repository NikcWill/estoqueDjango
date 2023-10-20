from django.shortcuts import render, HttpResponse
from.models import Products
 

def index(request):

  #return HttpResponse('Estou no Django')
  #from Product select *

  produtos = Products.objects.all()
  #for produto in produtos:
    #print(f'{produto.name} + {produto.price}')
  return render(request, 'pages/index.html', {'produtos':produtos})


def product_detail(request, id):
  product = Products.objects.get(id=id)
  return render(request, 'pages/product_detail.html', {'product': product})