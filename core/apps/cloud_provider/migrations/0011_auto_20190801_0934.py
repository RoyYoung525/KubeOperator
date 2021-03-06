# Generated by Django 2.1.2 on 2019-08-01 09:34

import common.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_provider', '0010_auto_20190801_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('vars', common.models.JsonDictTextField(default={})),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cloud_provider.Region')),
            ],
        ),
        migrations.RemoveField(
            model_name='zone',
            name='comment',
        ),
        migrations.AddField(
            model_name='plan',
            name='zones',
            field=models.ManyToManyField(to='cloud_provider.Zone'),
        ),
    ]
