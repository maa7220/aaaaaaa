# Generated by Django 4.1.6 on 2023-03-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nat_id',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]