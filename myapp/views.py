# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import Place, People


def demo(request):
    obj, obj1 = Place.objects.all, People.objects.all
    return render(request, "index.html", {'result': obj, 'person': obj1})
#
#
#
#
#
#
#
# def about(request):
#     return render(request, "about.html")
#
#
# def contact(request):
#     return render(request, "contact.html")


# def result(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     return render(request, "result.html",{'num1': x, 'num2': y, 'addition': add, 'subtraction': sub, 'multiplication': mul, 'division': div})
