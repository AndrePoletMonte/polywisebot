from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.keyboards.inline import lang_kb
from app.utils.i18n import _

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message, session: AsyncSession):
    user = await session.get(User, message.from_user.id)
    if not user:
        user = User(
            id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )
        session.add(user)
        await session.commit()
        
        await message.answer("Выберите язык / Choose language / Изаберите језик:", reply_markup=lang_kb)
    else:
        await message.answer(_("start", name=message.from_user.first_name), reply_markup=main_kb)

@router.callback_query(F.data.startswith("lang_"))
async def set_lang(callback: CallbackQuery, session: AsyncSession):
    lang = callback.data.split("_")[1]
    user = await session.get(User, callback.from_user.id)
    user.language = lang
    await session.commit()
    i18n.ctx_locale.set(lang)
    await callback.message.edit_text(_("start", name=callback.from_user.first_name), reply_markup=main_kb)

    )
    main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Статистика"), KeyboardButton(text="🔍 Помощь")],
        [KeyboardButton(text="🍪 Купить плюшку")]
    ],
    resize_keyboard=True
)