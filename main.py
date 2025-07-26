from aiogram import Bot, Dispatcher
from app.handlers import admin, payments
from app.middlewares.i18n_middleware import I18nMiddleware
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def on_startup(bot: Bot):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    base = os.getenv("RAILWAY_STATIC_URL", f"localhost:{os.getenv('PORT', 8080)}")
    webhook_url = f"https://{base}/{BOT_TOKEN}"
    await bot.set_webhook(webhook_url)
    dp.include_routers(start.router, echo.router, admin.router, payments.router)
    dp.update.middleware(DbSessionMiddleware())
dp.update.middleware(I18nMiddleware())