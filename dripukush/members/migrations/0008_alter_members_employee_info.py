# Generated by Django 3.2.12 on 2022-03-27 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20220328_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='employee_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_pro', to='members.office'),
        ),
    ]
