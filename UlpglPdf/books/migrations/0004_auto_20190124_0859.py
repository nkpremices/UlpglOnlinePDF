# Generated by Django 2.1.5 on 2019-01-24 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190121_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'ordering': ['value'], 'verbose_name': 'categorie'},
        ),
        migrations.RenameField(
            model_name='livre',
            old_name='image',
            new_name='cover',
        ),
        migrations.RenameField(
            model_name='livre',
            old_name='livre',
            new_name='pdf',
        ),
    ]
