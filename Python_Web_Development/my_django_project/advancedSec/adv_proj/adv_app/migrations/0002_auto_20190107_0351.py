# Generated by Django 2.1.5 on 2019-01-07 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adv_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
