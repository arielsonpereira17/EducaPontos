# Generated by Django 5.0 on 2024-11-22 23:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEduca', '0001_initial'),
        ('Desempenho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desempenho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desempenhos', to='AppEduca.aluno')),
            ],
        ),
    ]
