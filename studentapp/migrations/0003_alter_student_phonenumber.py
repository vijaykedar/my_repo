# Generated by Django 4.1.4 on 2022-12-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_alter_student_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phonenumber',
            field=models.BigIntegerField(verbose_name=30),
        ),
    ]
