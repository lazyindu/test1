import asyncio
import json
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums
from info import *
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@Client.on_message(filters.private & filters.regex(pattern=".*http.*") & filters.incoming)
async def download_video(client, message):
    url = message.text
    youtube_dl_username = None
    youtube_dl_password = None
    file_name = None
    if "|" in url:
        url_parts = url.split("|")
        if len(url_parts) == 2:
            url = url_parts[0]
            file_name = url_parts[1]
        elif len(url_parts) == 4:
            url = url_parts[0]
            file_name = url_parts[1]
            youtube_dl_username = url_parts[2]
            youtube_dl_password = url_parts[3]
        else:
            for entity in message.entities:
                if entity.type == "text_link":
                    url = entity.url
                elif entity.type == "url":
                    o = entity.offset
                    l = entity.length
                    url = url[o:o + l]
        if url is not None:
            url = url.strip()
        if file_name is not None:
            file_name = file_name.strip()
        # https://stackoverflow.com/a/761825/4723940
        if youtube_dl_username is not None:
            youtube_dl_username = youtube_dl_username.strip()
        if youtube_dl_password is not None:
            youtube_dl_password = youtube_dl_password.strip()
        logger.info(url)
        logger.info(file_name)
    else:
        for entity in message.entities:
            if entity.type == "text_link":
                url = entity.url
            elif entity.type == "url":
                o = entity.offset
                l = entity.length
                url = url[o:o + l]
    command_to_exec = [
        "yt-dlp",
        "--no-warnings",
        "--skip-download",
        "--youtube-skip-dash-manifest",
        "-j",
        url
    ]

    try:
        process = await asyncio.create_subprocess_exec(
            *command_to_exec,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()

        if e_response:
            error_message = e_response.replace(
                "please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output.", "")
            await message.reply_text(
                text=f"Error: {error_message}",
                parse_mode=enums.ParseMode.HTML,
                disable_web_page_preview=True
            )
            return

        if t_response:
            response_json = json.loads(t_response)
            inline_keyboard = []
            # logger.info(t_response)
            x_reponse = t_response
            dlocation = DOWNLOAD_LOCATION
            print(f"{dlocation}")
            if "\n" in x_reponse:
                x_reponse, _ = x_reponse.split("\n")
            response_json = json.loads(x_reponse)
            save_ytdl_json_path = DOWNLOAD_LOCATION + \
                "/" + str(message.from_user.id) + ".json"
            with open(save_ytdl_json_path, "w", encoding="utf8") as outfile:
                json.dump(response_json, outfile, ensure_ascii=False)
            # logger.info(response_json)
            inline_keyboard = []
            duration = None
            if "duration" in response_json:
                duration = response_json["duration"]
            if "formats" in response_json:
                for formats in response_json["formats"]:
                    format_id = formats.get("format_id")
                    format_string = formats.get("format_note")
                    if format_string is None:
                        format_string = formats.get("format")
                    format_ext = formats.get("ext")
                    cb_string_video = f"video|{format_id}|{format_ext}"
                    ikeyboard = [
                        InlineKeyboardButton(
                            f"🎬 {format_string} {format_ext}",
                            callback_data=cb_string_video.encode("UTF-8")
                        )
                    ]
                    inline_keyboard.append(ikeyboard)

            reply_markup = InlineKeyboardMarkup(inline_keyboard)
            await message.reply_text(
                text="Choose a format:",
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )

    except Exception as e:
        logger.error(f"An error occurred: {e}")
