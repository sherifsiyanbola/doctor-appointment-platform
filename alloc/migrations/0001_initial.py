# Generated by Django 2.2.4 on 2019-08-12 22:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('department', models.CharField(choices=[('csc', 'Computer Science'), ('it', 'Information Tecnology'), ('se', 'Software Engineering'), ('csec', 'Cyber Security')], max_length=100)),
                ('projecttype', models.CharField(choices=[('re', 'Research Work'), ('di', 'Design and Implementation')], max_length=100)),
                ('statement', models.TextField()),
                ('aims', models.TextField()),
                ('suplist', models.CharField(choices=[('prof', 'Prof Ahmad Baita Garko'), ('dean', 'Dr Abubakar Miyim'), ('hodcsc', 'Dr zaharadden'), ('kareem', 'Dr Abdulkareem'), ('lawan', 'Dr Abba Lawan'), ('kzr', 'Ahmad Sani Kazaure'), ('garko', 'Haruna Garko'), ('eng', 'Muhammad Abbas'), ('aml', 'Aminu Lawal'), ('mt', 'Muhammad Tukur Usman'), ('salisu', 'Sani Salisu')], max_length=100)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('manager', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
