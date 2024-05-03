# Generated by Django 5.0.4 on 2024-05-03 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_history', '0002_alter_medicalhistory_patient_id'),
        ('patients', '0003_patient_medical_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='medical_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_history.medicalhistory'),
        ),
    ]
