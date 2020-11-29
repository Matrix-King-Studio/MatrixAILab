# Generated by Django 3.1.3 on 2020-11-24 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tree', '0008_function_belongclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='belongClass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Tree.class', verbose_name='所属类'),
        ),
    ]
