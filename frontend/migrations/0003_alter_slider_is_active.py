# Generated by Django 4.2.1 on 2023-09-28 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_slider_is_showed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(choices=[(1, 'Is Active'), (0, 'Not Active')], default=False, help_text='Set one to true'),
        ),
    ]