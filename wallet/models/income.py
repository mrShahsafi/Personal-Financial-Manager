from django.db.models import (
    FloatField,
    ForeignKey,
    CASCADE,
)

from .base import AbstractModel


class Income(AbstractModel):
    wallet = ForeignKey(
        "Wallet",
        on_delete=CASCADE,
    )

    price = FloatField(
        default=0.0,
        verbose_name="the value of Income money",
        max_length=256,
    )
