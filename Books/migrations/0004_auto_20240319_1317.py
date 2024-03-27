# Generated by Django 3.2.12 on 2024-03-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_alter_book_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='book',
            name='book_covers',
            field=models.ImageField(null=True, upload_to='book_covers/'),
        ),
    ]
