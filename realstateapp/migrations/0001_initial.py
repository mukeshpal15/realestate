# Generated by Django 2.1.9 on 2020-04-08 07:22

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
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'agent_account',
            },
        ),
        migrations.CreateModel(
            name='PropertyCategoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_ID', models.CharField(max_length=100)),
                ('Category_Name', models.CharField(max_length=50)),
                ('Category_Image', models.ImageField(upload_to='categoryimages/')),
            ],
            options={
                'db_table': 'PropertyCategoryData',
            },
        ),
        migrations.CreateModel(
            name='PropertyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Property_ID', models.CharField(max_length=100)),
                ('Property_Name', models.CharField(max_length=100)),
                ('Property_About', models.CharField(max_length=1000)),
                ('Property_Price', models.CharField(max_length=50)),
                ('Property_Category', models.CharField(max_length=100)),
                ('Property_BuiltYear', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'PropertyData',
            },
        ),
        migrations.CreateModel(
            name='PropertyImagesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Property_ID', models.CharField(max_length=100)),
                ('Property_Image', models.ImageField(upload_to='propertyimages/')),
            ],
            options={
                'db_table': 'PropertyImagesData',
            },
        ),
    ]
