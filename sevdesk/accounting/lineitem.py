from __future__ import annotations

import datetime
from typing import TypeVar, Union, Dict, Any

import attr
import attrs

from .. import UNSET, Client, Unset
from ..client.models import PositionModel, PositionModelPart, PositionModelSevClient
from .discount import Discount
from .unity import Unity

T = TypeVar("T")


@attrs.define()
class LineItem:
    name: str
    "The name"
    quantity: float
    "Quantity of the item"
    price: float
    "The price of the item. You can either specify prices in gross or net, depending on the invoice settings."
    "Be careful not to mix things."
    tax: float
    "The tax-rate of the item"
    unity: Unity = Unity.PIECE
    "The unity of the item"
    discount: Union[Unset, Discount] = UNSET
    "An optional discount"
    text: Union[Unset, str] = UNSET
    "An optional text descriping the item"
    id: Union[Unset, int] = UNSET
    "The SevDesk internal id"
    create: Union[Unset, None, datetime.datetime] = UNSET
    update: Union[Unset, None, datetime.datetime] = UNSET
    part: Union[Unset, PositionModelPart] = UNSET
    priority: Union[Unset, int] = 100
    sev_client: Union[Unset, PositionModelSevClient] = UNSET
    position_number: Union[Unset, None, int] = UNSET
    temporary: Union[Unset, None, bool] = UNSET
    sum_net: Union[Unset, None, float] = UNSET
    sum_gross: Union[Unset, None, float] = UNSET
    sum_discount: Union[Unset, None, float] = UNSET
    sum_tax: Union[Unset, float] = UNSET
    sum_net_accounting: Union[Unset, None, float] = UNSET
    sum_tax_accounting: Union[Unset, None, float] = UNSET
    sum_gross_accounting: Union[Unset, None, float] = UNSET
    price_net: Union[Unset, None, float] = UNSET
    price_gross: Union[Unset, None, float] = UNSET
    price_tax: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def _get_api_model(self, client: Client, t: T) -> T:
        return t(
            id=self.id,
            name=self.name,
            quantity=self.quantity,
            tax_rate=self.tax,
            price=self.price,
            discounted_value=self.discount.value if self.discount else UNSET,
            unity=self.unity._get_api_model(client),
            is_percentage=self.discount.percentage if self.discount else UNSET,
            text=self.text,
            create=self.create,
            update=self.update,
            part=self.part,
            priority=self.priority,
            sev_client=self.sev_client,
            position_number=self.position_number,
            temporary=self.temporary,
            sum_net=self.sum_net,
            sum_gross=self.sum_gross,
            sum_discount=self.sum_discount,
            sum_tax=self.sum_tax,
            sum_net_accounting=self.sum_net_accounting,
            sum_tax_accounting=self.sum_tax_accounting,
            sum_gross_accounting=self.sum_gross_accounting,
            price_net=self.price_net,
            price_gross=self.price_gross,
            price_tax=self.price_tax,
            additional_properties=self.additional_properties,
        )

    @classmethod
    def _from_model(cls, client: Client, model: PositionModel) -> LineItem:
        return cls(
            name=model.name,
            quantity=float(model.quantity),
            price=float(model.price),
            tax=float(model.tax_rate),
            unity=Unity(model.unity.translation_code),
            discount=Discount(
                value=float(model.discounted_value),
                percentage=bool(int(model.is_percentage)),
            )
            if model.discounted_value is not None
            else UNSET,
            text=model.text if model.text is not None else UNSET,
            id=int(model.id),
            create=model.create,
            update=model.update,
            part=model.part,
            priority=model.priority,
            sev_client=model.sev_client,
            position_number=model.position_number,
            temporary=model.temporary,
            sum_net=model.sum_net,
            sum_gross=model.sum_gross,
            sum_discount=model.sum_discount,
            sum_tax=model.sum_tax,
            sum_net_accounting=model.sum_net_accounting,
            sum_tax_accounting=model.sum_tax_accounting,
            sum_gross_accounting=model.sum_gross_accounting,
            price_net=model.price_net,
            price_gross=model.price_gross,
            price_tax=model.price_tax,
        )
