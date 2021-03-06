# Generated by Django 4.0.4 on 2022-04-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=100)),
                ('request_date', models.DateField(auto_now=True)),
                ('student_dept', models.CharField(blank=True, max_length=100)),
                ('book_name', models.CharField(blank=True, max_length=100)),
                ('author_name', models.CharField(blank=True, max_length=100)),
                ('reason', models.CharField(blank=True, max_length=600)),
            ],
        ),
    ]
