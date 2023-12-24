# with Love @LazyDeveloperr 💘
# Subscribe YT @LazyDeveloperr - to learn more about this for free...

import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from info import UPDATES_CHANNEL
async def handle_force_subscribe(bot, message):
    try:
        invite_link = await bot.create_chat_invite_link(int(UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    try:
        user = await bot.get_chat_member(int(UPDATES_CHANNEL), message.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Sorry Sir, You are Banned. .",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=message.message_id,
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="**Please Join My Update Channel To Use Me**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✴️ Join My Update Channel ✴️", url=invite_link.invite_link)
                    ]
                ]
            ),
            parse_mode="markdown",
            reply_to_message_id=message.message_id,
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Something Went Wrong.",
            parse_mode="markdown",
            disable_web_page_preview=True,
            reply_to_message_id=message.message_id,
        )
        return 400


