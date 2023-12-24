    # Credit @LazyDeveloper.
    # Please Don't remove credit.
    # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
    # 🥰  Thank you for giving me credit @LazyDeveloperr  🥰

    # for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 

from pyrogram import Client, filters
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import random
import os
from PIL import Image

# the Strings used for this "thing"
from pyrogram import Client

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import filters
from database.lazy_ffmpeg import take_screen_shot
from info import DOWNLOAD_LOCATION, UPDATES_CHANNEL
from database.users_chats_db import db
from plugins.settings.settings import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from lazybot.forcesub import handle_force_subscribe
from database.add import add_user_to_database

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("😔**Sorry ! No thumbnail found...**😔") 


@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**Thumbnail deleted successfully**✅️")


@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    LazyDev = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await LazyDev.edit("**Thumbnail saved successfully**✅️")

# @Client.on_message(filters.private & filters.command(['urlthumb']))
# async def viewlazythumb(client, message):    
#     thumbnail = await db.get_lazy_thumbnail(message.from_user.id)
#     if not thumbnail:
#         await client.send_photo(
#         chat_id=message.chat.id, 
#         photo=thumbnail)
#     else:
#         await message.reply_text("😔**Sorry ! No thumbnail found...**😔")         

# @Client.on_message(filters.private & filters.command(['delurlthumb']))
# async def removelazythumb(client, message):
#     await db.set_lazy_thumbnail(message.from_user.id, None)
#     await message.reply_text("**Thumbnail deleted successfully**✅️")

# @Client.on_message(filters.private & filters.photo & filters.command(['set_url_thumb']))
# async def addlazythumbs(client, message):
#     LazyDev = await message.reply_text("Please Wait ...")
#     await db.set_lazy_thumbnail(message.from_user.id, thumbnail=message.photo.file_id)                
#     await LazyDev.edit("**Thumbnail saved successfully**✅️")


@Client.on_message(filters.private & filters.photo )
async def photo_handler(bot: Client, event: Message):
    if not event.from_user:
        return await event.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, event)
    if UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, event)
      if fsub == 400:
        return
    editable = await event.reply_text("**👀 Processing...**")
    await db.set_thumbnail(event.from_user.id, thumbnail=event.photo.file_id)
    await editable.edit("**✅ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sᴀᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!!**")

@Client.on_message(filters.private & filters.command(["delurlthumb", "deleteurlthumbnail"]))
async def delete_thumb_handler(bot: Client, event: Message):
    if not event.from_user:
        return await event.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, event)
    if UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, event)
      if fsub == 400:
        return

    await db.set_thumbnail(event.from_user.id, thumbnail=None)
    await event.reply_text(
        "**🗑️ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!!**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⚙ ᴄᴏɴғɪɢᴜʀᴇ sᴇᴛᴛɪɴɢs 👀", callback_data="OpenSettings")]
        ])
    )

@Client.on_message(filters.private & filters.command("showurlthumb") )
async def viewthumbnail(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update) 
    if UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
      if fsub == 400:
        return
    thumbnail = await db.get_lazy_thumbnail(update.from_user.id)
    if thumbnail is not None:
        await bot.send_photo(
        chat_id=update.chat.id,
        photo=thumbnail,
        caption=f"URL => ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴀᴠᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ 🦠",
        reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("🗑️ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ", callback_data="deleteurlthumbnail")]]
                ),
        reply_to_message_id=update.message_id)
    else:
        await update.reply_text(text=f"ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ғᴏᴜɴᴅ 🤒")

async def Gthumb01(bot, update):
    thumb_image_path = DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    db_thumbnail = await db.get_lazy_thumbnail(update.from_user.id)
    if db_thumbnail is not None:
        thumbnail = await bot.download_media(message=db_thumbnail, file_name=thumb_image_path)
        Image.open(thumbnail).convert("RGB").save(thumbnail)
        img = Image.open(thumbnail)
        img.resize((100, 100))
        img.save(thumbnail, "JPEG")
    else:
        thumbnail = None

    return thumbnail

async def Gthumb02(bot, update, duration, download_directory):
    thumb_image_path = DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    db_thumbnail = await db.get_lazy_thumbnail(update.from_user.id)
    if db_thumbnail is not None:
        thumbnail = await bot.download_media(message=db_thumbnail, file_name=thumb_image_path)
    else:
        thumbnail = await take_screen_shot(download_directory, os.path.dirname(download_directory), random.randint(0, duration - 1))

    return thumbnail

async def Mdata01(download_directory):

          width = 0
          height = 0
          duration = 0
          metadata = extractMetadata(createParser(download_directory))
          if metadata is not None:
              if metadata.has("duration"):
                  duration = metadata.get('duration').seconds
              if metadata.has("width"):
                  width = metadata.get("width")
              if metadata.has("height"):
                  height = metadata.get("height")

          return width, height, duration

async def Mdata02(download_directory):

          width = 0
          duration = 0
          metadata = extractMetadata(createParser(download_directory))
          if metadata is not None:
              if metadata.has("duration"):
                  duration = metadata.get('duration').seconds
              if metadata.has("width"):
                  width = metadata.get("width")

          return width, duration

async def Mdata03(download_directory):

          duration = 0
          metadata = extractMetadata(createParser(download_directory))
          if metadata is not None:
              if metadata.has("duration"):
                  duration = metadata.get('duration').seconds

          return duration
