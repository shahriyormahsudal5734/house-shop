from django.shortcuts import render
from .models import House
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView




def homepage(request):
    return render(request , 'index.html')


def detail(request):
    obj2 = House.objects.all()
    data = {
       'list2': obj2
    }
    return render(request , 'detail.html',context=data)


class Detailpage(DetailView):
    model =House
    template_name = 'detail_uy.html'


class Add(CreateView):
    model =House
    template_name = 'add.html'
    fields = '__all__'
    success_url = '/'