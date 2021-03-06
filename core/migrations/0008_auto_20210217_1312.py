# Generated by Django 3.1.6 on 2021-02-17 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210217_1231'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='Mails',
        ),
        migrations.DeleteModel(
            name='Meta',
        ),
        migrations.AlterField(
            model_name='project',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='core.service'),
        ),
    ]
