# Generated by Django 4.0.4 on 2022-04-30 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_requestbook_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestbook',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=100),
        ),
    ]