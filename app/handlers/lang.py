from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.inline import lang_kb

router = Router()

@router.message(F.text == "/language")
async def change_language(message: Message):
    await message.answer("Выберите язык:", reply_markup=lang_kb)