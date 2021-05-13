from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

def homepage(request):
    return render(request, "index.html") #Метод который отображает наш index файл


# def second(request):
#     return HttpResponse("Test2 page")

# def third(request):
#     return HttpResponse("This is page test3")