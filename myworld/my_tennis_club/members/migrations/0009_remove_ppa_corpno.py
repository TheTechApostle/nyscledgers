# Generated by Django 4.2 on 2024-04-26 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0008_corpregister"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ppa",
            name="corpNO",
        ),
    ]
