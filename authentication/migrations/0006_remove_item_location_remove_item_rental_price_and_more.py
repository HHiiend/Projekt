# Generated by Django 5.0.3 on 2024-05-16 21:45

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_booking_delete_rental'),
    ]

    operations = [
        #migrations.RemoveField(
        #    model_name='item',
        #    name='location',
        #),
        #migrations.RemoveField(
        #    model_name='item',
        #    name='rental_price',
        #),
        #migrations.RemoveField(
        #    model_name='item',
        #    name='status',
        #),
        #migrations.AddField(
        #    model_name='item',
        #    name='available',
        #    field=models.BooleanField(default=True),
        #),
        #migrations.AddField(
        #    model_name='item',
        #    name='created_at',
        #    field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
        #    preserve_default=False,
        #),
        #migrations.AddField(
        #    model_name='item',
        #    name='name',
        #    field=models.CharField(default=datetime.datetime(2024, 5, 16, 21, 45, 58, 634831, tzinfo=datetime.timezone.utc), max_length=255),
        #    preserve_default=False,
        #),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.booking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]