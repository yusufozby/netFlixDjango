# Generated by Django 4.1 on 2022-10-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_kategori_movies_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='video',
            field=models.FileField(null=True, upload_to='vidolar/'),
        ),
    ]
