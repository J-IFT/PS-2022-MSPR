from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/login.html')


def plant_list(request):
    return render(request, 'pages/plant_list.html')


def plant_detail(request, plant_id):
    return render(request, 'pages/plant_detail.html')


def offer_list(request):
    return render(request, 'pages/offer_list.html')


def offer_detail(request, offer_id):
    return render(request, 'pages/offer_detail.html')

def offer_add(request):
    return render(request, 'pages/offer_add.html')


def user_detail(request, user_id):
    return render(request, 'pages/user_detail.html')