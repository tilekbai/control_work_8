# Generated by Django 3.2 on 2021-05-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0002_auto_20210501_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.CharField(choices=[('Еда', 'food'), ('Обучение', 'education'), ('Одежда', 'clothes'), ('Электроника', 'electronic')], max_length=29, null=True, verbose_name='Категория'),
        ),
    ]
