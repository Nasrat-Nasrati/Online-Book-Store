# Generated by Django 3.2.12 on 2024-03-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_alter_book_category_delete_bookcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to='static/Cover_page/'),
        ),
    ]
