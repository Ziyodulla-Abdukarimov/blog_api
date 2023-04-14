# Generated by Django 4.2 on 2023-04-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_create_time_user_guid_user_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('CODE_VERIFIED', 'CODE_VERIFIED'), ('INFORMATION_FILLED', 'INFORMATION_FILLED'), ('DONE', 'DONE')], default='NEW', max_length=31),
        ),
    ]
