# Generated by Django 4.2.1 on 2023-09-28 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0001_initial'),
        ('matrixpro', '0016_alter_propertysalesmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrixproperty',
            name='posted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultants.consultant'),
        ),
    ]
