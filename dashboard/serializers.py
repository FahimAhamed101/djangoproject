from rest_framework import serializers
from .models import *

class TransactionListSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Transaction
        fields = '__all__'