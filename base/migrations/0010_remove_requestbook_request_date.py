# Generated by Django 4.0.4 on 2022-04-30 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_requestbook_date_of_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestbook',
            name='request_date',
        ),
    ]