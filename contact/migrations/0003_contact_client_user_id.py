# Generated by Django 2.2.6 on 2019-11-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_client_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_client',
            name='user_id',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
