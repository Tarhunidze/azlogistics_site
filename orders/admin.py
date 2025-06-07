from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'request_type')
    list_filter = ('request_type',)
    search_fields = ('full_name', 'phone', 'email')
