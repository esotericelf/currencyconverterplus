from rest_framework import serializers
from .models import Enquiry

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['index', 'user', 'buying_currency', 'selling_currency', 'amount', 'exchange_rate', 'date_of_entry']
