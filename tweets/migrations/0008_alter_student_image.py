# Generated by Django 4.0.3 on 2022-04-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default=True, null=True, upload_to='Images/'),
        ),
    ]
