# Generated by Django 4.1.10 on 2023-09-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_alter_signdata_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signdata',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
