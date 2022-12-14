# Generated by Django 4.1.3 on 2022-11-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stripecheckout", "0002_alter_discount_type_alter_tax_percentage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="type",
            field=models.CharField(
                choices=[
                    ("percentage", "Процентная скидка"),
                    ("fixed", "Фиксированная скидка"),
                ],
                default="percentage",
                max_length=32,
                verbose_name="Тип скидки",
            ),
        ),
    ]
