from django.shortcuts import render
from django.http import HttpResponse

def mostrar(resquest):
    return HttpResponse("ola mundo")