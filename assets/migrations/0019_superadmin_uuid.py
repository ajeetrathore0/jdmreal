# Generated by Django 4.1.7 on 2023-03-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0018_alter_check_user_type_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='superadmin',
            name='uuid',
            field=models.CharField(default=22, max_length=120),
            preserve_default=False,
        ),
    ]
