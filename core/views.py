from django.shortcuts import render ,HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(requests,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos </h1>'.format(nome,idade))

def soma(requests,n1,n2):
    resultado = n1+n2
    return HttpResponse('<h1>{}+{}= {}</h1>'.format(n1,n2,resultado))

def subt(requests,n1,n2):
    resultado = n1-n2
    return HttpResponse('<h1>{}-{}= {}</h1>'.format(n1,n2,resultado))

def mult(requests,n1,n2):
    resultado = n1*n2
    return HttpResponse('<h1>{}*{}= {}</h1>'.format(n1,n2,resultado))

def divi(requests,n1,n2):
    resultado = n1/n2
    return HttpResponse('<h1>{}/{}= {}</h1>'.format(n1,n2,resultado))