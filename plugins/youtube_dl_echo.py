import asyncio
import json
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@Client.on_message(filters.private & filters.regex(pattern=".*http.*") & filters.incoming)
async def echo(client, message):
    url = message.text

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
