from django.http import JsonResponse
import json
from .models import Anniversaire
from django.views.decorators.csrf import csrf_exempt
from datetime import date


def getAnniversaire(request):
    getAnniversaire = list(Anniversaire.objects.values())  
    return JsonResponse({"Liste des anniversaires": getAnniversaire})


def Anniversaire_today(request):
    today = date.today()
    anniversaires_today = list(Anniversaire.objects.filter(date_birthday__month=today.month, date_birthday__day=today.day).values())
    return JsonResponse({"Anniversaires aujourd'hui le " + str(today): anniversaires_today})


@csrf_exempt
def postAnniversaire(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) 
            anniv = Anniversaire.objects.create(
                name=data.get('name'),
                first_name=data.get('first_name'),
                genre=data.get('genre'),
                date_birthday=data.get('date_birthday'),
            )
            return JsonResponse({"message": "Anniversaire ajouté", "id": anniv.id})
        except Exception as e:
            return JsonResponse({"message": f"Erreur : {str(e)}"}, status=400)
    
    return JsonResponse({"message": "Méthode non autorisée"}, status=405)

