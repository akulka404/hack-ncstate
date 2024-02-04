# Generated by Django 3.2.23 on 2024-02-03 18:49

from django.db import migrations, models
import phone_field.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USERD',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=100)),
                ('user_age', models.IntegerField()),
                ('user_gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('/', 'Prefer not to say')], max_length=1)),
                ('user_contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('user_home_location', models.CharField(default='', max_length=100)),
                ('user_emergency_contact_name', models.CharField(default='', max_length=100)),
                ('user_emergency_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user_current_location', models.CharField(default='', max_length=100)),
                ('user_log_summarization', models.CharField(default='', max_length=100)),
            ],
        ),
    ]