# Generated by Django 4.0.5 on 2022-07-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postit_posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='picture'),
        ),
    ]