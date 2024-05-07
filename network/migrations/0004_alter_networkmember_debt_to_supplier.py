# Generated by Django 4.2 on 2024-05-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_networkmember_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkmember',
            name='debt_to_supplier',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='задолженность перед поставщиком'),
        ),
    ]