from django.shortcuts import render
from .models import *


def main(request):
    variant=Variant.objects.get(id=1)
    questions=variant.questions.all()
    return render(request,"main.html",{'list':questions})
