# Generated by Django 5.0.4 on 2024-04-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bu1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.IntegerField()),
                ('q2', models.IntegerField()),
                ('q3', models.IntegerField()),
                ('q4', models.IntegerField()),
                ('q5', models.IntegerField()),
            ],
        ),
    ]
