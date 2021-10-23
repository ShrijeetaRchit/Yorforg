import asyncio
from asyncio import sleep

from telethon import events
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins

from SaitamaRobot import telethn, OWNER_ID, DEV_USERS, DRAGONS, TIGERS

import html
from typing import Optional

from SaitamaRobot import LOGGER, TIGERS, dispatcher
from SaitamaRobot.modules.helper_funcs import chat_status

from telegram.ext.dispatcher import run_async

    user_admin = chat_status.user_admin
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

# =================== CONSTANT ===================

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

OFFICERS = [OWNER_ID] + DEV_USERS + DRAGONS + TIGERS

# Check if user has admin rights
async def is_administrator(user_id: int, message):
    admin = False
    async for user in telethn.iter_participants(
        message.chat_id, filter=ChannelParticipantsAdmins
    ):
        if user_id == user.id or user_id in OFFICERS:
            admin = True
            break
    return admin

@run_async
@admin
def zombies(event):
    """ For .zombies command, list all the zombies in a chat. """

    con = event.pattern_match.group(1).lower()
    del_u = 0
    del_status = "No Deleted Accounts Found, Group Is Clean."
     
