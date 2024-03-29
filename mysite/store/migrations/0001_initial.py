# Generated by Django 4.1.7 on 2023-03-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=60)),
                ('credit_card', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
