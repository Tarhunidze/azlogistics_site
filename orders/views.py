from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import OrderForm
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from .models import Order

def apply(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            # 🛡️ 1. АНТИСПАМ: проверка последних заявок по IP или Email
            recent_orders = Order.objects.filter(
                email=form.cleaned_data['email'],
                created_at__gte=timezone.now() - timedelta(minutes=1)
            )
            if recent_orders.exists():
                messages.error(request, "Пожалуйста, не отправляйте заявки слишком часто.")
                return redirect('apply')  # можно сделать stay-on-page с сообщением

            # 💾 2. СОХРАНЕНИЕ
            order = form.save()

            # 📩 3. ОТПРАВКА ПИСЬМА
            send_mail(
                subject='Новая заявка с сайта 8AZ Logistics',
                message=(
                    f"ФИО: {order.full_name}\n"
                    f"Телефон: {order.phone}\n"
                    f"Email: {order.email}\n"
                    f"Тип заявки: {order.get_request_type_display()}\n"
                    f"Комментарий: {order.message}"
                ),
                from_email='director@8az.kz',
                recipient_list=['director@8az.kz'],
                fail_silently=False,
            )

            return redirect('success_page')
    else:
        form = OrderForm()

    return render(request, 'orders/apply.html', {'form': form})
