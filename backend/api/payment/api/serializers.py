
from rest_framework import serializers
from backend.api.order.api.serializers import OrderSerializer


class CreditCardSerializer(serializers.Serializer):
    card_type = serializers.CharField(max_length=50)
    expiration_date = serializers.SerializerMethodField()
    last_4 = serializers.IntegerField()
    cardholder_name = serializers.CharField(max_length=100)

    def get_expiration_date(self, obj):
        exp_month = obj.expiration_month
        exp_year = obj.expiration_year
        return '{month}/{year}'.format(month=exp_month, year=exp_year)


class TransactionSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=50)
    amount = serializers.DecimalField(max_digits=7, decimal_places=2)
    created_at = serializers.DateTimeField()
    credit_card_details = CreditCardSerializer(many=False)
