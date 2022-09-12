from django.shortcuts import render
from .models import *

def home(request):
    rate = RateStars.objects.filter(score=2).order_by("?").first()
    context = {
        "rate": rate
    }
    return render(request, 'home.html', context)