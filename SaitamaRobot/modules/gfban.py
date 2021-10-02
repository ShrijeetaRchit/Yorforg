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

def stealgf(user: User,
         chat: Chat,
         message: Message,
    if bot_admin(chat, user.id):
        # message.reply_text("you can't steal Gf of a Sudo")
        return

    if user.id in DRAGON:
        if angel:
            message.reply_text(" you can't stole gf of a sudo.")
        return
    if user.id in OWNER:
       if angel:
           message.reply_text("Devil belongs to only one girl no chnace of you here")
       return

    if angel:
        angel_tag = mention_html(angel.id, angel.first_name)


@run_async
@user_admin
def give_gf(update: Update, context: CallbackContext) -> str:
    args = context.args
    message: Optional[Message] = update.effective_message
    chat: Optional[Chat] = update.effective_chat
    angel: Optional[User] = update.effective_user

    user_id

    if user_id:
        if (message.reply_to_message and
                message.reply_to_message.from_user.id == user_id):
            return girlfriend(
                message.reply_to_message.from_user,
                chat,
                message.reply_to_message,
                angel,
            )
        else:
            return girlfriend(
                chat.get_member(user_id).user, chat, message, angel)
    else:
        message.reply_text("That looks like an invalid User ID to me.")
    return ""


@run_async
@bot_admin
def gfban(update: Update, context: CallbackContext) -> str:
    args = context.args
    message: Optional[Message] = update.effective_message
    chat: Optional[Chat] = update.effective_chat
    user: Optional[User] = update.effective_user

    user_id = extract_user(message, args)

    if user_id:
        sql.gfban(user_id, chat.id)
        message.reply_text("user lost all his GFS and is accused for cheating")
        gfbanned = chat.get_member(user_id).user
        return (f"<b>{html.escape(chat.title)}:</b>\n"
                f"#GFbanned\n"
                f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
                f"<b>User:</b> {mention_html(gfbanned.id, gfbanned.first_name)}")
    else:
        message.reply_text("No user has been designated!")
    return ""


@run_async
def gfs(update: Update, context: CallbackContext):
    args = context.args
    message: Optional[Message] = update.effective_message
    chat: Optional[Chat] = update.effective_chat
    user_id = extract_user(message, args) or update.effective_user.id
    result = sql.get_gf(user_id, chat.id)

    if result and result[0] != 0:
        num_gf

        if reasons:
            text = (
                f"This user have {num_gf} girlfriends"
            )

            msgs = split_message(text)
            for msg in msgs:
                update.effective_message.reply_text(msg)
        else:
            


__mod_name__ = "Gfbans"

GIVEGF_HANDLER = CommandHandler("givegf", give_gf)
GFBAN_HANDLER = CommandHandler("gfban", gfban)
GFS_HANDLER = CommandHandler ("gfs", gfs)


dispatcher.add_handler(GIVEGF_HANDLER)
dispatcher.add_handler(GFBAN_HANDLER)
dispatcher.add_handler(GFS_HANDLER)
