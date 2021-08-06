from django.shortcuts import render
from .models import Expert


# Create your views here.
def lizards(request):
    return render(request, 'lizards.html', {
        'active_menu': 'about',
        'sub_menu': 'lizards',
    })


def commentator(request):
    experts = Expert.objects.all()
    return render(request, 'commentator.html', {
        'active_menu': 'about',
        'sub_menu': 'commentator',
        'experts': experts,
    })
