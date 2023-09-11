from aiogram.types import LabeledPrice
from aiogram import types

POST_REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title='Почтой',
    prices=[LabeledPrice('Стандартная упаковка', 0),
            LabeledPrice('Доставка почтой', 500_00)]
)

POST_FAST_SHIPPING = types.ShippingOption(
   id='post_fast',
   title='Доставка курьером',
   prices=[LabeledPrice('Прочная упаковка', 200_00),
       LabeledPrice('Доставка курьером', 1000_00)]
)

PICKUP_FAST_SHIPPING = types.ShippingOption(
   id='pickup',
   title='Самовывоз',
   prices=[LabeledPrice('Самовывоз из магазина', -100_00)]
)
