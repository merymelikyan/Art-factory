# Generated by Django 5.1.1 on 2024-09-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_footertext_link_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headertext',
            options={'verbose_name': 'Header Text', 'verbose_name_plural': 'Header Text'},
        ),
        migrations.AlterModelOptions(
            name='leftblock',
            options={'verbose_name': 'Left Block', 'verbose_name_plural': 'Left Block'},
        ),
        migrations.AlterModelOptions(
            name='miniblock3',
            options={'verbose_name': 'Mini Block3', 'verbose_name_plural': 'Mini Block3'},
        ),
        migrations.AlterModelOptions(
            name='miniblocks',
            options={'verbose_name': 'Mini Blocks', 'verbose_name_plural': 'Mini Blocks'},
        ),
        migrations.AlterModelOptions(
            name='rightblock',
            options={'verbose_name': 'Right Block', 'verbose_name_plural': 'Right Block'},
        ),
        migrations.AlterField(
            model_name='footertext',
            name='link_name',
            field=models.TextField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='leftblock',
            name='link_name',
            field=models.TextField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='miniblock3',
            name='image',
            field=models.ImageField(upload_to='mini-block3'),
        ),
        migrations.AlterField(
            model_name='miniblock3',
            name='link_name',
            field=models.TextField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='miniblocks',
            name='image',
            field=models.ImageField(upload_to='mini-blocks'),
        ),
        migrations.AlterField(
            model_name='rightblock',
            name='image',
            field=models.ImageField(upload_to='right-block'),
        ),
    ]