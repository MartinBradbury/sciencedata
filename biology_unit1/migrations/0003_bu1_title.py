# Generated by Django 5.0.4 on 2024-04-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biology_unit1', '0002_alter_bu1_q1'),
    ]

    operations = [
        migrations.AddField(
            model_name='bu1',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
