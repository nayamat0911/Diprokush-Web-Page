# Generated by Django 3.2.12 on 2022-03-30 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0020_alter_zoonlist_zoon_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('payIntro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payintro', to='members.members')),
            ],
        ),
    ]
