# Generated by Django 2.2 on 2020-08-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_book_book_seller_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]