from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.keyboards.inline import admin_panel_kb, back_admin
from app.utils.config import ADMIN_IDS

router = Router()

# фильтр на админов
router.message.filter(F.from_user.id.in_(ADMIN_IDS))
router.callback_query.filter(F.from_user.id.in_(ADMIN_IDS))

@router.message(F.text == "/admin")
async def admin_cmd(message: Message):
    await message.answer("Админ-панель:", reply_markup=admin_panel_kb)

@router.callback_query(F.data == "admin_stats")
async def stats(callback: CallbackQuery, session: AsyncSession):
    total = await session.scalar(select(func.count(User.id)))
    await callback.message.edit_text(f"Всего пользователей: {total}", reply_markup=back_admin)

# простые заглушки для бана/рассылки
@router.callback_query(F.data == "admin_ban")
async def ban_stub(callback: CallbackQuery):
    await callback.answer("Функция «Бан» пока не реализована", show_alert=True)

@router.callback_query(F.data == "admin_unban")
async def unban_stub(callback: CallbackQuery):
    await callback.answer("Функция «Разбан» пока не реализована", show_alert=True)

@router.callback_query(F.data == "admin_broadcast")
async def broadcast_stub(callback: CallbackQuery):
    await callback.answer("Функция «Рассылка» пока не реализована", show_alert=True)

@router.callback_query(F.data == "admin_back")
async def back(callback: CallbackQuery):
    await callback.message.edit_text("Админ-панель:", reply_markup=admin_panel_kb)