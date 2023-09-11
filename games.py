from dataclasses import dataclass
from aiogram.types import LabeledPrice
from typing import List
Pay_token = '1744374395:TEST:7b5173c3bf66679a519f'

@dataclass
class Genre:
    title: str
    description: str
    start_parameter: str
    currency: str
    prices: List[LabeledPrice]
    provider_data: dict = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    send_phone_number_to_provider: bool = False
    send_email_to_provider: bool = False
    is_flexible: bool = False
    provider_token: str = Pay_token

    def generate_invoices(self):
        return self.__dict__

ACTION = Genre(
    title='GTA V',
    description='Легендарное продолжение популярной серии Grand Theft Auto. Местом действия стал город Лос-Сантос, полюбившийся ещё в GTA: San Andreas. Впервые игра расскажет историю сразу трех персонажей: Майкла, Тревора и Франклина, между которыми вы сможете переключаться в любое время.',
    currency='RUB',
    prices=[
        LabeledPrice(label='GTA V', amount=3_000_00),
        LabeledPrice(label='Скидка',amount=-150_00)
    ],
    start_parameter='create_invoice_gta',
    photo_url="https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png",
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True
)

MMO = Genre(
    title='World of Warcraft',
    description='World of Warcraft – одна из популярнейших MMORPG, созданная компанией Blizzard в 2004 году. Эта многопользовательская онлайн-игра является прямым продолжением серии компьютерных игр Warcraft, разработанных той же студией.',
    currency='RUB',
    prices=[LabeledPrice(label='GTA V', amount=3_000_00),
        LabeledPrice(label='Скидка', amount=-150_00)
    ],
    start_parameter='create_invoice_world_of_warcraft',
    photo_url="https://www.goha.ru/s/f/Be/kR/4ohhndc2gs.jpg",
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True
)

RPG = Genre(
    title='Ведьмак 3: Дикая Охота',
    description='Даже профессиональному охотнику на чудовищ не скрыться от войны и политики, лжи и предательств. «Ведьмак 3: Дикая охота» посылает тебя в мрачный мир, созданный по мотивам произведений Анджея Сапковского. Под твоим контролем окажется сам Геральт, которому предстоит вновь отыскать своё предназначение.',
    currency='RUB',
    prices=[
        LabeledPrice(label='GTA V', amount=3_000_00),
        LabeledPrice(label='Скидка', amount=-150_00)
    ],
    start_parameter='create_invoice_witcher',
    photo_url="https://upload.wikimedia.org/wikipedia/ru/a/a2/The_Witcher_3-_Wild_Hunt_Cover.jpg",
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True
)