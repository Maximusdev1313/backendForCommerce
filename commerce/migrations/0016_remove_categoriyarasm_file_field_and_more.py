# Generated by Django 4.0.3 on 2022-07-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0015_alter_product_kilogramm_alter_product_litri_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriyarasm',
            name='file_field',
        ),
        migrations.RemoveField(
            model_name='productrasmi',
            name='file_field',
        ),
        migrations.AddField(
            model_name='categoriyarasm',
            name='link',
            field=models.CharField(default=1657014218235, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productrasmi',
            name='link',
            field=models.CharField(default=1657014218235, max_length=500),
            preserve_default=False,
        ),
    ]
