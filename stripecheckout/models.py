from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    """Item model that represents a single item on the site."""

    CURRENCY_ITEM = [
        ("USD", "usd"),
        ('RUB', 'rub'),
    ]

    name = models.CharField(
        verbose_name="Наименование товара",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
    )
    price = models.FloatField(
        verbose_name="Цена",
        max_length=25,
        validators=[MinValueValidator(0.0)],
    )
    currency = models.CharField(
        verbose_name="Валюта товара",
        choices=CURRENCY_ITEM,
        default="USD",
        max_length=10,
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name

    @property
    def price_in_cents(self):
        """The function of determining the price of an item in cents."""
        return self.price * 100


class Discount(models.Model):
    """Discount model for the Order."""

    TYPE_DISCOUNT = [
        ("PERCENTAGE", "percentage"),
        ("FIXED", "fixed"),
    ]

    name = models.CharField(
        verbose_name="Название скиди",
        max_length=255,
    )
    amount = models.FloatField(
        verbose_name="Размер скидки",
        max_length=25,
        validators=[MinValueValidator(0.0)],
    )
    type = models.CharField(
        verbose_name="Тип скидки",
        max_length=32,
        choices=TYPE_DISCOUNT,
        default="PERCENTAGE",
    )

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return self.name

    @property
    def amount_in_cents(self):
        """Function to determine the discount amount in cents."""
        return self.amount * 100


class Tax(models.Model):
    """Tax model for the Order."""
    name = models.CharField(
        verbose_name="Название налога",
        max_length=255,
    )
    percentage = models.PositiveSmallIntegerField(
        verbose_name="Процентная ставка",
        default=13,
    )

    class Meta:
        verbose_name = "Tax"
        verbose_name_plural = "Taxes"

    def __str__(self):
        return self.name


class Order(models.Model):
    """Order model that contains different items to buy."""
    items = models.ManyToManyField(
        Item,
        verbose_name="Список товаров",
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Скидка",
    )
    tax = models.ForeignKey(
        Tax,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Налог",
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        default_related_name = "orders"

    @property
    def total_price(self):
        """The function of determining the total price of the order."""
        total_price = 0.0
        for item in self.items.all():
            total_price += item.price_in_cents

        if self.discount is not None:
            discount = self.discount.amount
            if self.discount.type == 'percentage':
                total_price = total_price * (100 - discount) / 100
            else:
                total_price = total_price - self.discount.amount_in_cents

        if self.tax is not None:
            tax = self.tax.percentage
            total_price += total_price * tax / 100

        return round(total_price)

    @property
    def total_price_in_dollars(self):
        """The function to get the total order price in dollars."""
        return int(self.total_price) / 100
