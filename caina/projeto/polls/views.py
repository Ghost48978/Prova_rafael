from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Livro, Emprestimo

def index(request):
    questions = Livro.objects.all()
    emprestimo=Emprestimo.objects.all()
    context = {"questions": questions}
    return render(request, "polls/index.html", context)


    