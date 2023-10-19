from django.shortcuts import render, HttpResponse
from.models import Products
 

def index(request):

  #return HttpResponse('Estou no Django')
  #from Product select *

  produtos = Products.objects.all()
  #for produto in produtos:
    #print(f'{produto.name} + {produto.price}')
  return render(request, 'pages/index.html', {'produtos':produtos})