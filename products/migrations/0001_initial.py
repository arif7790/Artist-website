# Generated by Django 3.2 on 2022-08-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_pice', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('P', 'painting'), ('S', 'statuary'), ('H', 'Handicrafts'), ('M', 'Minatory')], max_length=4)),
                ('product_image', models.ImageField(upload_to='productimg')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
