from django.core.management import BaseCommand
from django.db import transaction

from addresses.models import Address
from clients.models import Client
from order_items.models import OrderItem
from orders.models import Order
from products.models import Product
from suppliers.models import Supplier


class Command(BaseCommand):
    help = 'Seed Initial'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            p1 = Product(name="Notebook", price=1500.00)
            p2 = Product(name="Impressora", price=800.00)
            p3 = Product(name="Mouse", price=80.00)

            p1.save()
            p2.save()
            p3.save()

            cli1 = Client(name="Maria Silva", email="maria@gmail.com")
            cli2 = Client(name="Paulo Silva", email="paulo@gmail.com")
            sup = Supplier(name="João Souza", email="joao@gmail.com")

            cli1.save()
            cli2.save()
            sup.save()

            add1 = Address(number="300", complement="Apto 203", zip_code="05577200", client=cli1)
            add2 = Address(number="600", complement="Apto 603", zip_code="05577200", client=cli2)

            add1.save()
            add2.save()

            order1 = Order(address_of_delivery=add1, supplier=sup)
            order2 = Order(address_of_delivery=add2, supplier=sup)

            order1.save()
            order2.save()

            oi1 = OrderItem(order=order1, product=p1, discount=0.0, quantity=1, price=2000.00)
            oi2 = OrderItem(order=order1, product=p3, discount=0.0, quantity=1, price=2000.00)
            oi3 = OrderItem(order=order1, product=p2, discount=100.00, quantity=1, price=800.00)

            oi1.save()
            oi2.save()
            oi3.save()
