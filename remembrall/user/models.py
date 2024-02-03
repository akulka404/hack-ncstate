from django.db import models
from datetime import timedelta
# from six import python_2_unicode_compatible
from multiselectfield import MultiSelectField
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField

class USERD(models.Model):
    user_id = models.AutoField(primary_key=True)

    user_name = models.CharField(max_length=100, blank=False, default='')

    user_age = models.IntegerField()

    REGISTER_CHOICES = (('F', 'Female'), ('M', 'Male'), ('/', 'Prefer not to say'),)
    user_gender = models.CharField(max_length=1, choices=REGISTER_CHOICES)
    
    user_contact = PhoneField(blank=True, help_text='Contact phone number')

    user_home_location = models.CharField(max_length=100, blank=False, default='')

    user_emergency_contact_name = models.CharField(max_length=100, blank=False, default='')

    user_emergency_contact = PhoneField(blank=True, help_text='Contact phone number')

    user_current_location = models.CharField(max_length=100, blank=False, default='')

    user_log_summarization = models.CharField(max_length=100, blank=False, default='')

    REGISTER_CHOICES = (('American Indian', 'American Indian'), ('Asian', 'Asian'), ('African American', 'African American'), ('Native Hawaiian', 'Native Hawaiian'), ('White', 'White'),)
    user_race = models.CharField(max_length=32, choices=REGISTER_CHOICES)
    
    def get_absolute_url(self):
        return reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[str(self.id), 'unique_identifier'])


class Meta:
    ordering = ['user_id']
