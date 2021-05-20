# Generated by Django 3.1.7 on 2021-05-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(upload_to='pics')),
                ('news_date', models.CharField(max_length=100)),
                ('news_title', models.CharField(max_length=100)),
                ('news_description', models.TextField()),
                ('news_url', models.CharField(max_length=300)),
            ],
        ),
    ]