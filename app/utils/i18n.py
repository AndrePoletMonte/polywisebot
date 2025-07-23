from pathlib import Path
from aiogram.utils.i18n import FluentRuntimeI18n

i18n = FluentRuntimeI18n(
    path=Path(__file__).parent.parent / "locales",
    default_locale="ru",
    domain="bot"
)
_ = i18n.gettext