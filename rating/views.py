from pickle import FALSE
from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def home(request):
    rate = RateStars.objects.filter(score=3).order_by("?").first()
    context = {
        "rate": rate
    }
    return render(request, 'home.html', context)

def rate_img(request):
    if request.method == "POST":
        el_id = request.POST.get("el_id")
        val = request.POST.get("val")
        rate = RateStars.objects.get(id=el_id)
        rate.score = val
        rate.save()
        return JsonResponse({"success": "true", "score": val}, safe=False)
    return JsonResponse({"success": "false"})