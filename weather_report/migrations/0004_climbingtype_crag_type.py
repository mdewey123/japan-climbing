# Generated by Django 5.0.4 on 2025-02-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_report', '0003_crag_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClimbingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='crag',
            name='type',
            field=models.ManyToManyField(blank=True, null=True, to='weather_report.climbingtype'),
        ),
    ]
