# Generated by Django 4.0.2 on 2022-03-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_alter_zoonlist_zoon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoonlist',
            name='zoon_name',
            field=models.CharField(choices=[('------', '----select----'), ('Dhaka', 'Dhaka'), ('Chittangog', 'Chittangog'), ('Cumilla', 'Cumilla'), ('Maymoshing', 'Maymoshing'), ('Syllet', 'Syllet'), ('Power plant', 'Power plant')], max_length=200),
        ),
    ]
