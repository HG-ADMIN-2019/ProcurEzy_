# Generated by Django 3.1.7 on 2023-09-25 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eProc_Configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectEfforts',
            fields=[
                ('project_efforts_guid', models.CharField(db_column='PROJECT_EFFORTS_GUID', max_length=32, primary_key=True, serialize=False)),
                ('project_id', models.CharField(db_column='PROJECT_ID', max_length=20)),
                ('username', models.CharField(db_column='USERNAME', max_length=16)),
                ('calender_id', models.CharField(db_column='CALENDER_ID', max_length=10)),
                ('project_category', models.CharField(db_column='PROJECT_CATEGORY', max_length=100)),
                ('effort', models.PositiveIntegerField(db_column='EFFORT', null=True)),
                ('effort_day', models.CharField(blank=True, db_column='EFFORT_DAY', max_length=10, null=True)),
                ('effort_date', models.DateField(db_column='EFFORT_DATE')),
                ('effort_week', models.PositiveIntegerField(db_column='EFFORT_WEEK', null=True)),
                ('effort_year', models.PositiveIntegerField(db_column='EFFORT_YEAR', null=True)),
                ('effort_description', models.CharField(db_column='EFFORT_DESCRIPTION', max_length=255)),
                ('project_efforts_created_by', models.CharField(db_column='PROJECT_EFFORTS_CREATED_BY', max_length=30, null=True)),
                ('project_efforts_created_at', models.DateTimeField(db_column='PROJECT_EFFORTS_CREATED_AT', max_length=50, null=True)),
                ('project_efforts_changed_by', models.CharField(db_column='PROJECT_EFFORTS_CHANGED_BY', max_length=30, null=True)),
                ('project_efforts_changed_at', models.DateTimeField(db_column='project_efforts_changed_at', max_length=50, null=True)),
                ('del_ind', models.BooleanField(db_column='DEL_IND', default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
            ],
            options={
                'db_table': 'MTD_PROJECT_EFFORTS',
                'managed': True,
            },
        ),
    ]
