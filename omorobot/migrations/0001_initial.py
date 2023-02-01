# Generated by Django 4.1.5 on 2023-02-01 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MycarAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mycar_speed', models.IntegerField(default=0, null=True)),
                ('mycar_battery', models.IntegerField(default=0, null=True)),
                ('mycar_color', models.TextField(null=True)),
                ('mycar_encoder_or', models.IntegerField(default=0, null=True)),
                ('mycar_encoder_ac', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('check_time', models.IntegerField(default=0, null=True)),
                ('user_name', models.ForeignKey(db_column='user_name', on_delete=django.db.models.deletion.CASCADE, to='omorobot.user')),
            ],
        ),
        migrations.CreateModel(
            name='Mycar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mycar_speed', models.IntegerField(default=0, null=True)),
                ('mycar_battery', models.IntegerField(default=0, null=True)),
                ('mycar_color', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_name', models.ForeignKey(db_column='user_name', on_delete=django.db.models.deletion.CASCADE, to='omorobot.user')),
            ],
        ),
    ]
