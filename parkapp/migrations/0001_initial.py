# Generated by Django 4.0.5 on 2022-06-21 09:41

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
            name='BookedSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=244)),
            ],
        ),
        migrations.CreateModel(
            name='ParkSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='parkslots/')),
                ('booked', models.BooleanField(default=False)),
                ('booked_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkapp.bookedslot')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(null=True, upload_to='profiles/')),
                ('phone_number', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('car_plate', models.CharField(max_length=20)),
                ('car_model', models.CharField(max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkapp.location')),
                ('parking_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkapp.parkslot')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
