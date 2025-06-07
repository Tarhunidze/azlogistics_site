from django.db import models

class Application(models.Model):
    SERVICE_CHOICES = [
        ('delivery', 'Грузоперевозка'),
        ('outsourcing', 'Аутсорсинг логистики'),
        ('multimodal', 'Мультимодальные перевозки'),
        ('special', 'Спецтехника'),
        ('other', 'Другое'),
    ]

    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=30)
    email = models.EmailField("Email")
    service_type = models.CharField("Тип услуги", max_length=50, choices=SERVICE_CHOICES)
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.service_type})"
