# Generated by Django 3.0.4 on 2020-03-08 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_a', models.CharField(max_length=10)),
                ('value_b', models.FloatField(max_length=10)),
                ('result', models.CharField(max_length=10)),
            ],
        ),
    ]
