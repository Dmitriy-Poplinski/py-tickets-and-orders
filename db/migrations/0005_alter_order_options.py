# Generated by Django 4.0.2 on 2024-02-08 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
    ]