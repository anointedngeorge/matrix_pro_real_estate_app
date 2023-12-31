# Generated by Django 4.2.1 on 2023-09-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixpro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertysalesmodel',
            name='pro_location',
        ),
        migrations.RemoveField(
            model_name='propertysalesmodel',
            name='pro_qty',
        ),
        migrations.RemoveField(
            model_name='propertysalesmodel',
            name='pro_title',
        ),
        migrations.RemoveField(
            model_name='propertysalesmodel',
            name='pro_type',
        ),
        migrations.AlterField(
            model_name='propertysalesmodel',
            name='pro_actual_qty',
            field=models.CharField(blank=True, help_text='enter qty o purchase', max_length=150, null=True, verbose_name='property actual quantity'),
        ),
    ]
