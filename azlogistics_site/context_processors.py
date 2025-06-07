from django.utils import timezone

def current_year(request):
    return {
        'now': timezone.now()
    }
