from app.handlers import admin, payments
from app.middlewares.i18n_middleware import I18nMiddleware
dp.update.middleware(DbSessionMiddleware())
dp.update.middleware(I18nMiddleware())
dp.include_routers(start.router, echo.router, admin.router, payments.router)
