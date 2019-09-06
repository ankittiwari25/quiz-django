# Generated by Django 2.0.12 on 2019-09-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0013_advancejava'),
    ]

    operations = [
        migrations.CreateModel(
            name='Android',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='questions',
            name='catagory',
            field=models.CharField(choices=[('java', 'Java'), ('c', 'C'), ('python', 'Python'), ('android', 'Android')], max_length=20),
        ),
    ]
