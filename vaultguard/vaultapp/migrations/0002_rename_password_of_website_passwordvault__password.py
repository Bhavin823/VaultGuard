# Generated by Django 5.0.4 on 2024-06-24 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaultapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwordvault',
            old_name='password_of_website',
            new_name='_password',
        ),
    ]
