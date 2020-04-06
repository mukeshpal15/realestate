# Generated by Django 2.1.1 on 2020-04-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agent_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('aadhar', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'agent_account',
            },
        ),
    ]
