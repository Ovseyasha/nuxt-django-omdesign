# Generated by Django 3.1.6 on 2021-02-17 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210217_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='core.project'),
        ),
        migrations.AlterUniqueTogether(
            name='gallery',
            unique_together={('project',)},
        ),
    ]
