# Generated by Django 4.0.4 on 2022-04-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_requestbook_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]