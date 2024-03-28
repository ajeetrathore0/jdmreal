# Generated by Django 4.1.7 on 2023-05-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0022_rooms_show_places_delete_showplaces'),
    ]

    operations = [
        migrations.AddField(
            model_name='show_places',
            name='product_id',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='rooms',
            table='rooms',
        ),
        migrations.AlterModelTable(
            name='show_places',
            table='show_places',
        ),
    ]
