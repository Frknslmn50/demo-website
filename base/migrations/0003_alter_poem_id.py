# Generated by Django 5.0.6 on 2024-06-17 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_date_created_poem_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]