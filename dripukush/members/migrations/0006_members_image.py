# Generated by Django 3.2.12 on 2022-03-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20210828_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='image',
            field=models.ImageField(blank=True, upload_to='member/member_img'),
        ),
    ]
