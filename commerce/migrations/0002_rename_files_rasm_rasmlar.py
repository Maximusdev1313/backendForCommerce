# Generated by Django 4.0.3 on 2022-06-28 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rasm',
            old_name='files',
            new_name='rasmlar',
        ),
    ]
