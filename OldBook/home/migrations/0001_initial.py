# Generated by Django 2.2.7 on 2019-11-28 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('title', models.CharField(max_length=99)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('writer', models.CharField(max_length=49)),
                ('sellerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
            ],
        ),
        migrations.CreateModel(
            name='giveAway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('buyerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyers', to='login.user')),
                ('sellerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='login.user')),
            ],
            options={
                'unique_together': {('bookID', 'sellerID', 'buyerID')},
            },
        ),
        migrations.CreateModel(
            name='exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyerBookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyerBook', to='home.book')),
                ('buyerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='login.user')),
                ('sellerBookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellerBook', to='home.book')),
                ('sellerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='login.user')),
            ],
            options={
                'unique_together': {('sellerBookID', 'buyerBookID', 'sellerID', 'buyerID')},
            },
        ),
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('buyerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
            ],
            options={
                'unique_together': {('bookID', 'buyerID')},
            },
        ),
    ]
