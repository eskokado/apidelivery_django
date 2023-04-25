from django.core.exceptions import ObjectDoesNotExist

from addresses.models import Address
from addresses.serializers import AddressSerializer
from clients.models import Client
from order_items.models import OrderItem
from orders.models import Order
from orders.serializers import OrderSerializer, OrderResponseSerializer, OrderItemResponseSerializer
from products.models import Product
from products.serializers import ProductSerializer
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer


def create_delivery_response(order, order_item):
    order_data = OrderResponseSerializer(order).data
    order_item_data = OrderItemResponseSerializer(order_item).data

    order_data["address_of_delivery"] = AddressSerializer(order.address_of_delivery).data
    order_data["supplier"] = SupplierSerializer(order.supplier).data
    order_item_data["product"] = ProductSerializer(order_item.product).data

    response = {
        'order': order_data,
        'order_items': [order_item_data],
        'errors': [],
        'status_code': 201
    }

    return response


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

            serialized_order = OrderResponseSerializer(order).data
            serialized_order['address_of_delivery'] = AddressSerializer(address).data
            serialized_order['supplier'] = SupplierSerializer(supplier).data

            serialized_order_item = OrderItemResponseSerializer(order_item).data
            serialized_order_item['product'] = ProductSerializer(product).data

            delivery_response['order'] = serialized_order
            delivery_response['order_items'].append(serialized_order_item)
        except ObjectDoesNotExist:
            delivery_response['errors'].append({'message': 'Objeto não encontrado', 'field': None})
            delivery_response['status_code'] = 400
        except Exception as e:
            delivery_response['errors'].append({'message': str(e), 'field': "None"})
            delivery_response['status_code'] = 400

        return delivery_response
