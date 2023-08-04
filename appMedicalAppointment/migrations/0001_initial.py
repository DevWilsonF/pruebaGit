# Generated by Django 4.2.4 on 2023-08-03 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appPatients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalAppointment',
            fields=[
                ('appointmentID', models.AutoField(primary_key=True, serialize=False)),
                ('appointmentDate', models.DateField(verbose_name='apointmentDate')),
                ('appointmentTime', models.TimeField(verbose_name='appointmentTime')),
                ('state', models.BooleanField(default=True)),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('patientID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPatients.patients')),
            ],
        ),
    ]
