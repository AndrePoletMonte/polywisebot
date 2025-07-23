from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import User
from app.utils.i18n import i18n

class I18nMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: TelegramObject, data: dict):
        session: AsyncSession = data["session"]
        user_id = data["event_from_user"].id
        res = await session.execute(select(User.language).where(User.id == user_id))
        lang = res.scalar_one_or_none() or "ru"
        i18n.ctx_locale.set(lang)
        data["locale"] = lang
        return await handler(event, data)