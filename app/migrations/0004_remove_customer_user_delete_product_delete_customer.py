# Generated by Django 4.1.6 on 2023-05-03 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
