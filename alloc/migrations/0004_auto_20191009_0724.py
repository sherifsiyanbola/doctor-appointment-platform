# Generated by Django 2.2.4 on 2019-10-09 07:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alloc', '0003_auto_20190915_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='suplist',
        ),
        migrations.AddField(
            model_name='project',
            name='first_choice_supervisor',
            field=models.CharField(choices=[('prof', 'Prof Ahmad Baita Garko'), ('dean', 'Dr Abubakar Miyim'), ('hodcsc', 'Dr zaharadden'), ('kareem', 'Dr Abdulkareem'), ('lawan', 'Dr Abba Lawan'), ('kzr', 'Ahmad Sani Kazaure'), ('garko', 'Haruna Garko'), ('eng', 'Muhammad Abbas'), ('aml', 'Aminu Lawal'), ('mt', 'Muhammad Tukur Usman'), ('salisu', 'Sani Salisu')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='second_choice_supervisor',
            field=models.CharField(choices=[('prof', 'Prof Ahmad Baita Garko'), ('dean', 'Dr Abubakar Miyim'), ('hodcsc', 'Dr zaharadden'), ('kareem', 'Dr Abdulkareem'), ('lawan', 'Dr Abba Lawan'), ('kzr', 'Ahmad Sani Kazaure'), ('garko', 'Haruna Garko'), ('eng', 'Muhammad Abbas'), ('aml', 'Aminu Lawal'), ('mt', 'Muhammad Tukur Usman'), ('salisu', 'Sani Salisu')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='third_choice_supervisor',
            field=models.CharField(choices=[('prof', 'Prof Ahmad Baita Garko'), ('dean', 'Dr Abubakar Miyim'), ('hodcsc', 'Dr zaharadden'), ('kareem', 'Dr Abdulkareem'), ('lawan', 'Dr Abba Lawan'), ('kzr', 'Ahmad Sani Kazaure'), ('garko', 'Haruna Garko'), ('eng', 'Muhammad Abbas'), ('aml', 'Aminu Lawal'), ('mt', 'Muhammad Tukur Usman'), ('salisu', 'Sani Salisu')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
