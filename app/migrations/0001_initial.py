# Generated by Django 4.0.5 on 2022-07-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('school_location', models.CharField(max_length=100)),
                ('school_principal', models.CharField(max_length=100)),
            ],
        ),
    ]
