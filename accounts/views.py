from django.shortcuts import render, HttpResponse,redirect
from django.contrib import auth, messages
from.models import User 
from random import randint

def user_login(request):

    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        

        userVerify = auth.authenticate(
            request, username=user, password=password)
        
        if userVerify == None:
            messages.info(request, 'Usuário ou senha incorretos seu tanso!')
            return redirect('login')
        else:
            auth.login(request, userVerify)
            return redirect('home')
    else:

        return render(request,'pages/login.html')

def add_user(request ):
  if request.method == 'POST':

    name = request.POST.get('name')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    cod = randint(100, 10000)
    in_stock = True

    User.objects.create(
      name=name, cod=cod, usuario=usuario, email=email,
      senha=senha, in_stock=in_stock
    )
    return redirect('home')
    
  else:
    return render(request,'pages/add-user.html')  
 
    