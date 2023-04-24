import ipdb
from django.core.exceptions import ObjectDoesNotExist

from addresses.models import Address
from clients.models import Client
from order_items.models import OrderItem
from order_items.serializers import OrderItemSerializer
from orders.models import Order
from orders.serializers import OrderSerializer
from products.models import Product
from suppliers.models import Supplier


class DeliveryService:

    @staticmethod
    def create_delivery(delivery_request):
        delivery_response = {
            'order': None,
            'order_items': [],
            'errors': [],
            'status_code': 0,
        }

        try:
            client = Client.objects.get(id=delivery_request['client_id'])
            supplier = Supplier.objects.get(id=delivery_request['supplier_id'])
            product = Product.objects.get(id=delivery_request['product_id'])
            address = Address.objects.get(client=client)

            order = Order(address_of_delivery=address, supplier=supplier)
            order.save()

            order_item = OrderItem(
                order=order,
                product=product,
                discount=delivery_request['discount'],
                quantity=delivery_request['quantity'],
                price=product.price
            )
            order_item.save()

            serialized_order = OrderSerializer(order).data
            serialized_order_item = OrderItemSerializer(order_item).data

            delivery_response['order'] = serialized_order
            delivery_response['order_items'].append(serialized_order_item)
            delivery_response['status_code'] = 201
        except ObjectDoesNotExist:
            delivery_response['errors'].append({'message': 'Objeto não encontrado', 'field': None})
            delivery_response['status_code'] = 400
        except Exception as e:
            delivery_response['errors'].append({'message': str(e), 'field': "None"})
            delivery_response['status_code'] = 400

        return delivery_response
