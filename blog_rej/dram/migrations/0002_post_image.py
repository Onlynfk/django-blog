# Generated by Django 2.1 on 2019-08-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]