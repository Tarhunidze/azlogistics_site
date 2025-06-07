from django.utils import timezone
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'now': timezone.now()})
