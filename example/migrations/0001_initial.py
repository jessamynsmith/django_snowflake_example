# Generated by Django 4.0.4 on 2022-05-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('R_REASON_SK', models.IntegerField(primary_key=True, serialize=False)),
                ('R_REASON_ID', models.CharField(max_length=16)),
                ('R_REASON_DESC', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.REASON',
                'managed': False,
            },
        ),
    ]
