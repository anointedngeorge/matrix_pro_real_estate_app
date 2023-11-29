# Generated by Django 4.2.1 on 2023-09-29 07:50

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('matrixpro', '0023_matrixpropertytype_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatrixPropertyFeatures',
            fields=[
                ('created', models.DateField(auto_created=True, default=django.utils.timezone.now, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Property Feature',
                'verbose_name_plural': 'Property Feature',
            },
        ),
        migrations.AddField(
            model_name='matrixproperty',
            name='property_features',
            field=models.ManyToManyField(blank=True, null=True, to='matrixpro.matrixpropertyfeatures'),
        ),
    ]