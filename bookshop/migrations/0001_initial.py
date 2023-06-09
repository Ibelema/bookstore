# Generated by Django 4.2.1 on 2023-05-07 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=15)),
                ('author', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=13)),
                ('content', models.TextField()),
            ],
        ),
    ]
