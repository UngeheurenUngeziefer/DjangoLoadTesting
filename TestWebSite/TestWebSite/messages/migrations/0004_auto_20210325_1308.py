# Generated by Django 3.1.7 on 2021-03-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plane_messages', '0003_auto_20210325_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(default='title', max_length=120),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.TextField(null=True),
        ),
    ]