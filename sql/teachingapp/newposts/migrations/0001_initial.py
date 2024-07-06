# Generated by Django 5.0.6 on 2024-07-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('postcontent', models.CharField(max_length=64)),
                ('posttitle', models.CharField(max_length=64)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]