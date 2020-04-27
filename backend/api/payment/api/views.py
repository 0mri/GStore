from django.conf import settings
import braintree
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TransactionSerializer
from backend.api.order.api.serializers import OrderSerializer

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY)

)

TRANSACTION_SUCCESS_STATUSES = [
    braintree.Transaction.Status.Authorized,
    braintree.Transaction.Status.Authorizing,
    braintree.Transaction.Status.Settled,
    braintree.Transaction.Status.SettlementConfirmed,
    braintree.Transaction.Status.SettlementPending,
    braintree.Transaction.Status.Settling,
    braintree.Transaction.Status.SubmittedForSettlement
]


@api_view(['GET'])
def get_client_token(request, *args, **kwargs):
    # try:
    #     return Response({"token": gateway.client_token.generate({
    #         "customer_id": request.user.id
    #     })})
    # except:
    return Response({"token": gateway.client_token.generate()})


def get_transaction(new_order, transaction_id):
    try:
        transaction = gateway.transaction.find(transaction_id)
    except:
        return Response({'error': 'Transaction Not Found'}, status=404)
    result = {}
    if transaction.status in TRANSACTION_SUCCESS_STATUSES:
        new_order.save(status='paid')
        result = {
            'status': 'success',
            'header': 'Success!',
            'message': 'You transaction has been successfully processed.'
        }
        # order cart!
    else:
        result = {
            'status': 'fail',
            'header': 'Transaction Failed',
            'message': 'Your transaction has a status of ' + transaction.status,

        }

    result['transaction'] = TransactionSerializer(transaction).data

    return Response(result)


@api_view(['POST'])
def make_payment(request):
    nonce_from_the_client = request.data.get('payment_method_nonce')
    products = request.data.get('products')

    amount = OrderSerializer().calc_amount(products)

    data = {
        'address': 'New CheckOUT MetHod AdDrEss',
        # 'products': [{'id': '1', 'quantity': "1"}]
        'products': products,
        'status': 'created',
        'order_total': amount
    }

    new_order = OrderSerializer(data=data, context={'request': request})

    if not new_order.is_valid():
        return Response(new_order.errors)

    result = gateway.transaction.sale({
        "amount": amount,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    if result.is_success or result.transaction:

        return get_transaction(new_order=new_order, transaction_id=result.transaction.id)

    return Response({'error': result.message}, status=402)
