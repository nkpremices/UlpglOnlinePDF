# Generated by Django 2.1.5 on 2019-01-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20190124_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livre',
            name='cover',
        ),
        migrations.AlterField(
            model_name='livre',
            name='pdf',
            field=models.FileField(upload_to='books/pdfs/'),
        ),
    ]
