# Generated by Django 5.0.3 on 2024-03-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('M', 'Masculine'), ('F', 'Femenine')], default='F', max_length=1),
        ),
    ]
