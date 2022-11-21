"""Stripecheckout URLs."""

from django.urls import path

from stripecheckout import views

app_name = "stripecheckout"

urlpatterns = [
    path("buy/<int:item_id>/", views.ItemBuyView.as_view(), name="buy-item"),
    path("item/<int:item_id>/", views.ItemView.as_view(), name="item"),
    path(
        "buy-order/<int:order_id>/",
        views.OrderBuyView.as_view(),
        name="buy-order"
    ),
    path("order/<int:order_id>/", views.OrderView.as_view(), name="order"),
]
