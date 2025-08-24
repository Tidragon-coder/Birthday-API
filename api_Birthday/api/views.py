from django.shortcuts import render
from django.http import JsonResponse

def bonjour(request):
    return JsonResponse({"message": "Bonjour, monde!"})
