# Generated by Django 2.2.7 on 2019-11-28 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminUser',
            fields=[
                ('name', models.CharField(max_length=48)),
                ('email', models.CharField(max_length=98)),
                ('password', models.CharField(max_length=98)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='login.user')),
            ],
        ),
    ]
