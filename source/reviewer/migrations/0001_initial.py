# Generated by Django 3.2 on 2021-05-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=60, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('category', models.CharField(choices=[('1', 'food'), ('2', 'education'), ('3', 'clothes'), ('4', 'electronic')], max_length=29, null=True, verbose_name='Категория')),
                ('picture', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'goods',
            },
        ),
    ]
