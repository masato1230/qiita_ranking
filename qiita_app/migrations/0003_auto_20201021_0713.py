# Generated by Django 3.1.2 on 2020-10-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qiita_app', '0002_result_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
