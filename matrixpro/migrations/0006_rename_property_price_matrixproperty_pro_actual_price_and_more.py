# Generated by Django 4.2.1 on 2023-09-23 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixpro', '0005_rename_property_qty_matrixproperty_property_total_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matrixproperty',
            old_name='property_price',
            new_name='pro_actual_price',
        ),
        migrations.RenameField(
            model_name='matrixproperty',
            old_name='property_price_currency',
            new_name='pro_actual_price_currency',
        ),
        migrations.RenameField(
            model_name='propertysalesmodel',
            old_name='pro_actual_price',
            new_name='pro_price',
        ),
        migrations.RemoveField(
            model_name='matrixproperty',
            name='property_total_qty',
        ),
        migrations.RemoveField(
            model_name='propertysalesmodel',
            name='pro_actual_qty',
        ),
        migrations.AddField(
            model_name='matrixproperty',
            name='pro_actual_qty',
            field=models.IntegerField(default=0, verbose_name='Property Actual qty'),
        ),
        migrations.AddField(
            model_name='propertysalesmodel',
            name='pro_qty',
            field=models.CharField(blank=True, help_text='enter qty purchase', max_length=150, null=True, verbose_name='property actual quantity'),
        ),
    ]
