# Generated by Django 3.2.12 on 2022-03-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_members_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='image',
            field=models.ImageField(blank=True, upload_to='member_pic'),
        ),
        migrations.AlterField(
            model_name='members',
            name='office_address',
            field=models.CharField(max_length=100),
        ),
    ]