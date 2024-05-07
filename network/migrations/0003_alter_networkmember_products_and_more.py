# Generated by Django 4.2 on 2024-05-04 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_product_options_networkmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkmember',
            name='products',
            field=models.ManyToManyField(blank=True, to='network.product', verbose_name='продукты объекта сети'),
        ),
        migrations.AlterField(
            model_name='networkmember',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.networkmember', verbose_name='поставщик объекта сети'),
        ),
    ]
