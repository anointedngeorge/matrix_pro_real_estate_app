# Generated by Django 4.2.1 on 2023-09-28 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixpro', '0017_matrixproperty_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrixproperty',
            name='property_state',
            field=models.CharField(choices=[('new', 'New'), ('outofstock', 'Out Of Stock'), ('rent', 'For Rent'), ('sale', 'For Sale')], default='new', max_length=150),
        ),
    ]
