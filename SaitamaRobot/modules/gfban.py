import html
import re
from typing import Optional

import telegram
from SaitamaRobot import DRAGONS, dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import (
    bot_admin,
    can_restrict,
    is_user_admin,
    user_admin,
    user_admin_no_reply,
)
from SaitamaRobot.modules.helper_funcs.extraction import (
    extract_text,
    extract_user,
    extract_user_and_text,
)
from SaitamaRobot.modules.helper_funcs.string_handling import split_quotes
from SaitamaRobot.modules.sql import gf_sql as sql
from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    DispatcherHandlerStop,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html



    if angel:
        angel_tag = mention_html(angel.id, angel.first_name)


def __import_data__(chat_id, data):
    for user_id, count in data.get("Girlfriend", {}).items():
        for x in range(int(count)):
            sql.stealed_user(user_id, chat_id)


__help__ = """
 • `/warns <userhandle>`*:* get a user's number, and reason, of warns.
"""

__mod_name__ = "Gfbans"

WARN_HANDLER = CommandHandler("warn", warn_user, filters=Filters.group)


dispatcher.add_handler(WARN_HANDLER)
 
