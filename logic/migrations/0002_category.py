# Generated by Django 4.2.6 on 2023-12-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='index/img')),
                ('name', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
