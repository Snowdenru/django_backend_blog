from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def book(request):
    return HttpResponse("Книга 1")


def main(request):
    context = {"user_name": "Denis", "message": "Hello World"}
    return render(request, "blog/main.html", context)

