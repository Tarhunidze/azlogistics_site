from django import forms
from .models import Order
import re

class OrderForm(forms.ModelForm):
    # скрытое поле для антиспама (боты его могут заполнять)
    extra_field = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'email', 'request_type', 'message']

    def clean_extra_field(self):
        if self.cleaned_data.get('extra_field'):
            raise forms.ValidationError("Spam detected.")
        return self.cleaned_data.get('extra_field')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_cleaned = re.sub(r"[ \-()]", "", phone)  # удалим пробелы, дефисы, скобки

        # Мягкая валидация международного формата
        if not re.match(r"^\+?\d{9,}$", phone_cleaned):
            raise forms.ValidationError("Введите корректный международный номер телефона.")
        return phone
