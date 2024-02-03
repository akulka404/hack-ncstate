from rest_framework import serializers
from user.models import USERD

class USERD_Serializer(serializers.ModelSerializer):
	class Meta:
		model = USERD
		fields = ('user_id', 'user_name', 'user_age', 
'user_gender', 'user_contact', 'user_home_location', 
'user_emergency_contact_name', 'user_emergency_contact', 
'user_current_location', 'user_log_summarization', 'user_race')
