# Generated by Django 2.1 on 2018-08-26 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20180826_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='name_org',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='repository',
            old_name='fecha_repo',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='repository',
            old_name='name_repo',
            new_name='name',
        ),
    ]