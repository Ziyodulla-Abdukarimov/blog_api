# Generated by Django 4.2 on 2023-04-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_auth_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_type',
            field=models.CharField(choices=[('via_email', 'via_email'), ('via_phone', 'via_phone'), ('via_username', 'via_username')], default='via_username', max_length=31),
        ),
    ]