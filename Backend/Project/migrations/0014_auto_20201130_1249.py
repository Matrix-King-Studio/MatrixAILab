# Generated by Django 3.1.3 on 2020-11-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0013_noderesult'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='value',
            field=models.TextField(blank=True, null=True, verbose_name='节点运行结果'),
        ),
        migrations.DeleteModel(
            name='NodeResult',
        ),
    ]