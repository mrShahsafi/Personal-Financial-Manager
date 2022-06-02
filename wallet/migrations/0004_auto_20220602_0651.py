# Generated by Django 3.1.7 on 2022-06-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20220602_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='currency',
            field=models.CharField(choices=[('Dollar', '$'), ('Toman', 'T')], default='T', max_length=6),
        ),
        migrations.AlterField(
            model_name='income',
            name='price',
            field=models.FloatField(default=0.0, max_length=256, verbose_name='the value of Income money'),
        ),
        migrations.AlterField(
            model_name='spend',
            name='price',
            field=models.FloatField(default=0.0, max_length=256, verbose_name='the value of Spent money'),
        ),
    ]
