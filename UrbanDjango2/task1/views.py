from django.shortcuts import render
from .forms import UserRegister
from .models import *
# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')

def games(request):
    games_all = Game.objects.all()
    # list = ['Atomic Heart',
    #  'Cyberpunk 2077',
    # 'PayDay 2']
    context = {
        'games_all': games_all
    }
    return render(request, 'fourth_task/games.html', context)

def cart (request):

    return render(request, 'fourth_task/cart.html')



#users = ["existing_user1", "existing_user2"]


buyers = Buyer.objects.all()

def handle_registration(form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    repeat_password = form.cleaned_data['repeat_password']
    age = form.cleaned_data['age']

    if password == repeat_password and int(age) >= 18 and not Buyer.objects.filter(name=username).exists():
        Buyer.objects.create(name=username, balance=2000.0, age=age)
        return {'message': f"Приветствуем, {username}!", 'form': UserRegister()}
    if password != repeat_password:
        return {'error': "Пароли не совпадают", 'form': form}
    elif age < '18':
        return {'error': "Вы должны быть старше 18", 'form': form}
    elif Buyer.objects.filter(name=username).exists():
        return {'error': "Пользователь уже существует", 'form': form}


    # else:
    #     Buyer.objects.create(name=username, balance=2000.0, age=age)
    #     return {'message': f"Приветствуем, {username}!", 'form': UserRegister()}


def sign_up_by_django(request):

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            result = handle_registration(form)
            return render(request, 'fifth_task/registration_page.html', result)
    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page.html', {'form': form})

