# Generated by Django 4.1.5 on 2023-09-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_house_voliyat_alter_house_manzil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryviloyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=200)),
            ],
        ),
    ]