"""Views for API / templates."""

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import DetailView

from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderBuyView(DetailView):
    model = Order
    pk_url_kwarg = "order_id"

    def get(self, request, *args, **kwargs):
        order = self.get_object()
        intent = self.get_intent(order)
        return JsonResponse({"client_secret": intent.client_secret})

    @staticmethod
    def get_intent(order):
        return stripe.PaymentIntent.create(
            amount=order.total_price,
            currency=order.currency,
            payment_method_types=["card"],
            metadata={"integration_check": "accept_a_payment"},
        )


class OrderView(DetailView):
    model = Order
    pk_url_kwarg = "order_id"
    context_object_name = "order"
    template_name = "order.html"


class ItemView(DetailView):
    model = Item
    pk_url_kwarg = "item_id"
    context_object_name = "item"
    template_name = "item.html"


class ItemBuyView(DetailView):
    model = Item
    pk_url_kwarg = "item_id"

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        intent = self.get_intent(item)
        return JsonResponse({"client_secret": intent.client_secret})

    @staticmethod
    def get_intent(item):
        return stripe.PaymentIntent.create(
            amount=item.price,
            currency=item.currency,
            payment_method_types=["card"],
            metadata={"integration_check": "accept_a_payment"},
        )
