# Generated by Django 5.0.7 on 2024-08-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vicodin', '0004_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='producto_images/'),
        ),
    ]
