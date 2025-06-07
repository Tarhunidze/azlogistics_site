from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import OrderForm


def apply(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            # 📩 Отправка письма администратору
            send_mail(
                subject='Новая заявка с сайта 8AZ Logistics',
                message=(
                    f"ФИО: {order.full_name}\n"
                    f"Телефон: {order.phone}\n"
                    f"Email: {order.email}\n"
                    f"Тип заявки: {order.get_request_type_display()}\n"
                    f"Комментарий: {order.message}"
                ),
                from_email='director@8az.kz',  # или тот, что указал в settings
                recipient_list=['director@8az.kz'],  # ⚠️ замени на свою почту
                fail_silently=False,
            )

            return redirect('success_page')
    else:
        form = OrderForm()

    return render(request, 'orders/apply.html', {'form': form})


def success_page(request):
    return render(request, 'orders/success.html')
