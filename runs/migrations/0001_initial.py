# Generated by Django 3.1.3 on 2021-03-20 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runner_name', models.CharField(max_length=25)),
                ('runner_surname', models.CharField(max_length=25)),
                ('runner_date_of_birth', models.DateField()),
                ('runner_email', models.CharField(max_length=25)),
                ('runner_phone', models.IntegerField()),
                ('registration_payment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RunDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_name', models.CharField(max_length=64)),
                ('run_city', models.CharField(max_length=25)),
                ('run_distance', models.IntegerField()),
                ('run_date', models.DateField()),
                ('active_registration', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RunType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserPrivateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_data', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='runs.registration')),
                ('user_runs', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='runs.rundetails')),
            ],
        ),
        migrations.AddField(
            model_name='rundetails',
            name='run_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runs.runtype'),
        ),
        migrations.AddField(
            model_name='registration',
            name='run_connection',
            field=models.ManyToManyField(to='runs.RunDetails'),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EC', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('telephone', models.IntegerField()),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runs.userprivatedata')),
            ],
        ),
    ]
