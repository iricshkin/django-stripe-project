from django.urls import path
from stripecheckout import views

app_name = 'stripecheckout'

urlpatterns = [
    path('items/<int:item_id>/buy', views.ItemBuyView.as_view()),
    path('items/<int:item_id>/', views.ItemView.as_view()),
]
