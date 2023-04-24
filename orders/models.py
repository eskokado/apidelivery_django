from django.db import models

from django.db import models
from django.utils import timezone
from enum import Enum, unique


@unique
class StateDelivery(Enum):
    PENDING = (1, "Pendente")
    DELIVERED = (2, "Entregue")
    CANCELED = (3, "Cancelado")

    def __init__(self, code, description):
        self._code = code
        self._description = description

    @property
    def code(self):
        return self._code

    @property
    def description(self):
        return self._description

    @classmethod
    def to_enum(cls, code):
        if code is None:
            return None
        for state in cls:
            if code == state.code:
                return state
        raise ValueError(f"Id inválido: {code}")


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    state_delivery = models.IntegerField(default=1)

    class Meta:
        db_table = 'orders'

    @property
    def state_delivery_enum(self):
        return StateDelivery.to_enum(self.state_delivery)

    @state_delivery_enum.setter
    def state_delivery_enum(self, state_delivery):
        self.state_delivery = state_delivery.code
