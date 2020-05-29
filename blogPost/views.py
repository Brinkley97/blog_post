from django.shortcuts import render
import requests


#homepage
def homepage(request):
    return render(request, "index.html")
