from rest_framework.views import APIView
from rest_framework.response import Response
from apps.orders.models import Order
from .models import Payment
from .serializers import PaymentSerializer


class CreatePaymentView(APIView):

    def post(self, request):

        order_id = request.data.get("order_id")

        order = Order.objects.get(id=order_id)

        payment, created = Payment.objects.get_or_create(
            order=order,
            defaults={"amount": order.total_price}
        )

        serializer = PaymentSerializer(payment)

        return Response({
            "message": "Payment created",
            "payment": serializer.data
        })
    

class ConfirmPaymentView(APIView):

    def post(self, request):

        payment_id = request.data.get("payment_id")

        payment = Payment.objects.get(id=payment_id)

        payment.status = "successful"
        payment.transaction_id = "SIMULATED_TXN_123"
        payment.save()

        # update order
        order = payment.order
        order.status = "paid"
        order.save()

        return Response({"message": "Payment successful"})
    
    

from rest_framework.permissions import IsAuthenticated

class CartView(APIView):
    permission_classes = [IsAuthenticated]