# Generated by Django 4.2.1 on 2023-09-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixpro', '0012_alter_propertysalesmodel_pro_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertysalesmodel',
            name='discount_currency',
        ),
        migrations.AlterField(
            model_name='propertysalesmodel',
            name='balance',
            field=models.FloatField(blank=True, editable=False, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='propertysalesmodel',
            name='discount',
            field=models.FloatField(default=0.0, max_length=300),
        ),
    ]
