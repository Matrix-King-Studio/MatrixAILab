# Generated by Django 3.1.3 on 2020-11-19 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_graph_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='graph',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Project.graph'),
            preserve_default=False,
        ),
    ]
