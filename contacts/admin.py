from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'get_service_display', 'created_at')
    list_filter = ('service_type', 'created_at')
    search_fields = ('name', 'phone', 'email', 'comment')

    def get_service_display(self, obj):
        return dict(Application.SERVICE_CHOICES).get(obj.service_type, obj.service_type)
    get_service_display.short_description = 'Услуга'
