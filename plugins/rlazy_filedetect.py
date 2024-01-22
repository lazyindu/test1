#     # Credit @LazyDeveloper.
#     # Please Don't remove credit.
#     # Born to make history @LazyDeveloper !

#     # Thank you LazyDeveloper for helping us in this Journey
#     # 🥰  Thank you for giving me credit @LazyDeveloperr  🥰

#     # for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 

# from pyrogram import Client, filters
# from pyrogram.enums import MessageMediaType
# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply


# @Client.on_message(filters.private & filters.reply)
# async def refunc(client, message):
#     reply_message = message.reply_to_message
#     if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
#         new_name = message.text 
#         await message.delete() 
#         msg = await client.get_messages(message.chat.id, reply_message.id)
#         file = msg.reply_to_message
#         media = getattr(file, file.media.value)
#         if not "." in new_name:
#             if "." in media.file_name:
#                 extn = media.file_name.rsplit('.', 1)[-1]
#             else:
#                 extn = "mkv"
#             new_name = new_name + "." + extn
#         await reply_message.delete()

#         button = [[InlineKeyboardButton("📁 Dᴏᴄᴜᴍᴇɴᴛ",callback_data = "upload_document")]]
#         if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
#             button.append([InlineKeyboardButton("🎥 Vɪᴅᴇᴏ", callback_data = "upload_video")])
#         elif file.media == MessageMediaType.AUDIO:
#             button.append([InlineKeyboardButton("🎵 Aᴜᴅɪᴏ", callback_data = "upload_audio")])
#         await message.reply(
#             text=f"**Sᴇʟᴇᴄᴛ Tʜᴇ Oᴜᴛᴩᴜᴛ Fɪʟᴇ Tyᴩᴇ**\n**• Fɪʟᴇ Nᴀᴍᴇ :-**```{new_name}```",
#             reply_to_message_id=file.id,
#             reply_markup=InlineKeyboardMarkup(button)
#         )

#     # if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
#     #     new_name = message.text
#     #     await message.delete()
#     #     media = await client.get_messages(message.chat.id, reply_message.id)
#     #     file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
#     #     filename = file.file_name
#     #     types = file.mime_type.split("/")
#     #     mime = types[0]
#     #     mg_id = media.reply_to_message.id
#     #     try:
#     #         out = new_name.split(".")
#     #         out[1]
#     #         out_name = out[-1]
#     #         out_filename = new_name
#     #         await message.reply_to_message.delete()
#     #         if mime == "video":
#     #             markup = InlineKeyboardMarkup([[
#     #                 InlineKeyboardButton("📁 Document", callback_data="upload_document"),
#     #                 InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
#     #         elif mime == "audio":
#     #             markup = InlineKeyboardMarkup([[InlineKeyboardButton(
#     #                 "📁 Document", callback_data="doc"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
#     #         else:
#     #             markup = InlineKeyboardMarkup(
#     #                 [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]])
#     #         # Lazy-WarninG -> Please Dont chnage anything after this Line 
#     #         await message.reply_text(f"**Select the output file type**\n**🎞New Name** :- ```{out_filename}```", reply_to_message_id=mg_id, reply_markup=markup)

#     #     except:
#     #         try:
#     #             out = filename.split(".")
#     #             out_name = out[-1]
#     #             out_filename = new_name + "." + out_name
#     #         except:
#     #             await message.reply_to_message.delete()
#     #             await message.reply_text("**Error** :  No  Extension in File, Not Supporting", reply_to_message_id=mg_id)
#     #             return
#     #         await message.reply_to_message.delete()
#     #         if mime == "video":
#     #             markup = InlineKeyboardMarkup([[InlineKeyboardButton(
#     #                 "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
#     #         elif mime == "audio":
#     #             markup = InlineKeyboardMarkup([[InlineKeyboardButton(
#     #                 "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
#     #         else:
#     #             markup = InlineKeyboardMarkup(
#     #                 [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]])
#     #         # Lazy-WarninG -> Please Dont chnage anything after this Line 
#     #         await message.reply_text(f"**Select the output file type**\n**🎞New Name** :- ```{out_filename}```",
#     #                                  reply_to_message_id=mg_id, reply_markup=markup)
