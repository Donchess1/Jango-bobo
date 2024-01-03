from django.shortcuts import render
from django.http import JsonResponse

def my_view(request):
    data = {
        "Name": "Abodunrin Stephen",
        "github_url": "github.com/Donchess1",
        "Gender": "Male",
        }
    return JsonResponse(data)
# Create your views here.
