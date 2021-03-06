# Generated by Django 3.2.6 on 2021-08-27 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('post', models.CharField(choices=[('Excutive Engineer', 'Excutive Engineer'), ('Sub-Divisional Engineer', 'Sub-Divisional Engineer'), ('Assistant Engineer', 'Assistant Engineer'), ('Sub-Assistant Engineer', 'Sub-Assistant Engineer')], max_length=150)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=17)),
                ('nationality', models.CharField(max_length=30)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Buddist', 'Buddist'), ('Chisttran', 'Chisttran'), ('Others', 'Others')], max_length=50)),
                ('biodata', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='session/profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
