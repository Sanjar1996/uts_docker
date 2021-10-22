# Generated by Django 3.2.8 on 2021-10-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCarusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=350)),
                ('sub_title', models.CharField(max_length=450)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='PriceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=75)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Xodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('occupation', models.CharField(max_length=150)),
                ('images', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=75)),
                ('title', models.ManyToManyField(to='articles.PriceModel')),
            ],
        ),
    ]
