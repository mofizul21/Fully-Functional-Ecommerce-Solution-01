from django.shortcuts import render, redirect
from django.http import HttpResponse

# models
from payment.models import BillingAddress
from order.models import Cart, Order

# view
from django.views.generic import TemplateView


class CheckoutTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = BillingAddress(instance=saved_address)

        context = {
            'billing_address': form,
        }
        return render(request, 'store/checkout.html', context)

    def post(self, request, *args, **kwargs):
        pass









































