# Generated by Django 2.2.10 on 2021-09-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='mail',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
