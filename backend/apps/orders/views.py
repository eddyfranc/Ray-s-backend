from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart, CartItem, Order, OrderItem
from apps.catalog.models import ProductVariant
from .serializers import CartSerializer, OrderSerializer


class CartView(APIView):

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    

class AddToCartView(APIView):

    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)

        variant_id = request.data.get("variant_id")
        quantity = request.data.get("quantity", 1)

        variant = ProductVariant.objects.get(id=variant_id)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            variant=variant
        )

        if not created:
            item.quantity += int(quantity)

        item.save()

        return Response({"message": "Item added to cart"})
    

class CreateOrderView(APIView):

    def post(self, request):

        cart = Cart.objects.get(user=request.user)

        order = Order.objects.create(user=request.user)

        total = 0

        for item in cart.items.all():

            OrderItem.objects.create(
                order=order,
                variant=item.variant,
                price=item.variant.price,
                quantity=item.quantity,
            )

            total += item.variant.price * item.quantity

        order.total_price = total
        order.save()

        cart.items.all().delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data)