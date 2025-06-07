from django.urls import path
from .views import apply, success_page

urlpatterns = [
    path('', apply, name='apply'),
    path('success/', success_page, name='success_page'),
]