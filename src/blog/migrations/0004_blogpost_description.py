# Generated by Django 2.2 on 2019-10-02 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.TextField(default='Bla bla bla'),
        ),
    ]