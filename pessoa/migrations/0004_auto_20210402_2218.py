# Generated by Django 3.1.7 on 2021-04-03 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
        ('pessoa', '0003_auto_20210402_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='enderecopessoa',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant'),
            preserve_default=False,
        ),
    ]