# Generated by Django 4.0.4 on 2022-04-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_requestbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestbook',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]