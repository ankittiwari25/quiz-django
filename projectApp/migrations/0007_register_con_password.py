# Generated by Django 2.2.1 on 2019-08-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0006_register_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='con_password',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
