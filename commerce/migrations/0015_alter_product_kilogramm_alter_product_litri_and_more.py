# Generated by Django 4.0.3 on 2022-07-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0014_rename_rasm_categoriyarasm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kilogramm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='litri',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='narx',
            field=models.FloatField(),
        ),
    ]
