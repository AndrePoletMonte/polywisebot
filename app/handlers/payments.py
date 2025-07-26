from aiogram import Router, F
from aiogram.types import (
    Message, LabeledPrice, PreCheckoutQuery, SuccessfulPayment
)
from app.keyboards.inline import buy_keyboard

router = Router()

ITEM_NAME = "Плюшка"
PRICE = 50  # 50 Stars

@router.message(F.text == "🍪 Купить плюшку")
async def send_invoice(message: Message):
    await message.answer_invoice(
        title=ITEM_NAME,
        description="Самая вкусная виртуальная плюшка",
        payload="buy_plushka",
        currency="XTR",
        prices=[LabeledPrice(label=ITEM_NAME, amount=PRICE)],
        reply_markup=buy_keyboard(ITEM_NAME, PRICE)
    )

@router.pre_checkout_query()
async def pre_checkout(query: PreCheckoutQuery):
    await query.answer(ok=True)

@router.message(F.successful_payment)
async def success_payment(message: Message):
    await message.answer("Спасибо за покупку! Плюшка отправлена в цифровой коробке 🎁")