# Generated by Django 4.1.3 on 2022-11-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stripecheckout", "0003_alter_discount_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="currency",
            field=models.CharField(
                choices=[("usd", "Доллары"), ("rub", "Рубли")],
                default="usd",
                max_length=10,
                verbose_name="Валюта товара",
            ),
        ),
    ]
