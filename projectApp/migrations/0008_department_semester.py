# Generated by Django 2.2.1 on 2019-08-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0007_register_con_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.IntegerField()),
                ('d_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('s_name', models.CharField(max_length=50)),
            ],
        ),
    ]