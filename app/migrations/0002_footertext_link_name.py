# Generated by Django 5.1.1 on 2024-09-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='footertext',
            name='link_name',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
