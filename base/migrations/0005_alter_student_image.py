# Generated by Django 4.0.4 on 2022-04-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='./media/user_icon_400x472.png', upload_to=''),
        ),
    ]
