# Generated by Django 3.2 on 2021-10-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('Twitter', models.URLField(blank=True, null=True)),
                ('about', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Information',
                'verbose_name_plural': 'Information',
                'managed': True,
            },
        ),
    ]
