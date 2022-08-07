from unicodedata import name
from django.shortcuts import render, HttpResponse

from . models import myuploadfile

# Create your views here.


def index(request):
    return render(request, "index.html")


def send_fills(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        for f in myfile:
            myuploadfile(f_name=name, myfiles=f).save()

        return HttpResponse("ok")
