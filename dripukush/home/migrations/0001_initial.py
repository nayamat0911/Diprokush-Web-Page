# Generated by Django 4.0.2 on 2022-02-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=250)),
                ('image', models.ImageField(upload_to='home/home_img')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
