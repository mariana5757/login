from django.shortcuts import render, HttpResponse
from .models import User
from .forms import CreateUser, Login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import auth

# Create your views here.


def register(request):
    form = CreateUser(request.POST or None)
    message = ''
    if (request.method == 'POST'):
        name = request.POST['name']
        user = request.POST['user']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if (User.objects.filter(user=user).exists()):
            message = 'El usuario ya existe'
        elif (password != confirm_password):
            message = 'Las contraseñas no coninciden'
        else:
            password2 = make_password(password)
            User.objects.create(name=name, user=user, password=password2)
            message = 'Guardado con éxito'
    return render(request, 'index.html', {
        'form': form,
        'message': message
    })


def login(request):
    form = Login(request.POST or None)
    message = ''
    if (request.method == 'POST'):
        user = request.POST['user']
        if (User.objects.filter(user=user).exists()):
            user_get = User.objects.get(user=user)
            encryptedpassword = user_get.password
            password = request.POST['password']
            checkpassword = check_password(password, encryptedpassword)
            print(encryptedpassword)
            print(password)
            print(checkpassword)
            if (checkpassword):
                message = 'Entra'
                return render(request, 'home.html')
            else:
                message = 'Contraseña incorrecta'
        else:
            message = 'el usuario no existe'
    return render(request, 'index.html', {
        'form': form,
        'message': message
    })

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

