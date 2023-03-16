from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    catefory_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, Cupcake!'
    context_dict['categories'] = catefory_list
    return render(request, 'rango/index.html', context=context_dict)


