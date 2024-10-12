from rest_framework import serializers
from .models import ClickTransactionPR

class ClickTransactionSerilaizerPR(serializers.ModelSerializer):
    class Meta():
        model = ClickTransactionPR
        fields = '__all__'