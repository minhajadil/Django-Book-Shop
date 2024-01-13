# Generated by Django 5.0.1 on 2024-01-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_remove_comment_name_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='Books.category'),
        ),
    ]