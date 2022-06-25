from django.db.models import (
    FloatField,
    ForeignKey,
    CASCADE,
)

from .base import AbstractModel


class Invest(AbstractModel):
    wallet = ForeignKey(
        "Wallet",
        on_delete=CASCADE,
    )
    price = FloatField(
        default=0.0,
        verbose_name="the value of Invest money",
        max_length=256,
    )

    def __str__(self):
        return f"{self.name} - {self.price}"
