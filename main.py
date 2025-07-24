import os
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def on_startup(bot: Bot):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    base = os.getenv("RAILWAY_STATIC_URL", f"localhost:{os.getenv('PORT', 8080)}")
    webhook_url = f"https://{base}/{BOT_TOKEN}"
    await bot.set_webhook(webhook_url)