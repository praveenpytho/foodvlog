# Generated by Django 4.1.3 on 2023-07-12 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_catog_slug_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catog',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
