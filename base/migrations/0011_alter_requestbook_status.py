# Generated by Django 4.0.4 on 2022-04-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_requestbook_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestbook',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
