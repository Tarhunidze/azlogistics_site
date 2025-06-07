from django.db import models

class Order(models.Model):
    REQUEST_TYPES = [
        ('cargo', 'Грузоперевозка'),
        ('storage', 'Складские услуги'),
        ('customs', 'Таможенное оформление'),
    ]

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.request_type}"
