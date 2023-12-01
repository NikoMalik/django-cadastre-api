from rest_framework import serializers
from .models import QueryHistory

class QueryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryHistory
        fiels = '__all__'
        
        