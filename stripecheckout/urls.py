from django.urls import path

from stripecheckout import views

app_name = "stripecheckout"

urlpatterns = [
    path("buy/<int:item_id>/", views.ItemBuyView.as_view()),
    path("item/<int:item_id>/", views.ItemView.as_view()),
]
