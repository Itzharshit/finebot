# (c) Code-X-Mania 
from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
import logging
logger = logging.getLogger(__name__)

from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)



@StreamBot.on_message((filters.command("start") | filters.regex('startβ‘οΈ')) & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**#NEW_USER:** \nA new user started [{m.from_user.first_name}](tg://user?id={m.from_user.id})  @filestreamprobot!!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "start" or "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="You are banned, contact @pyrogrammers",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                 await StreamBot.send_photo(
                    chat_id=m.chat.id,
                    photo="https://i.ibb.co/NKXgXD4/vlmnwosn-0.png",
                    caption="<i>πΉπΎπΈπ½ CHANNEL ππΎ πππ΄ πΌπ΄π</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Jα΄ΙͺΙ΄ Ι΄α΄α΄‘ π", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                 return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>An error occurred</i> <b>Contact @pyrogrammers</b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await StreamBot.send_photo(
            chat_id=m.chat.id,
            photo ="https://user-images.githubusercontent.com/88939380/137127129-a86fc939-2931-4c66-b6f6-b57711a9eab7.png",
            caption ="""Hello !
I am file stream bot, I can play your video file in your browser.
You can also add me to your movie or video channel to get stream and download button for your file.""",
            parse_mode="html",
            )
                                                                                       
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**You are banned, contact @pyrogrammers",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await StreamBot.send_photo(
                    chat_id=m.chat.id,
                    photo="https://i.ibb.co/ys3Tgpk/mtzijuhd-0.png",
                    caption="**PΚα΄α΄sα΄ Jα΄ΙͺΙ΄  Uα΄α΄α΄α΄α΄s CΚα΄Ι΄Ι΄α΄Κ α΄α΄ α΄sα΄ α΄ΚΙͺs Bα΄α΄**!\n\n**Dα΄α΄ α΄α΄ Oα΄ α΄ΚΚα΄α΄α΄, OΙ΄ΚΚ CΚα΄Ι΄Ι΄α΄Κ Sα΄Κsα΄ΚΙͺΚα΄Κs α΄α΄Ι΄ α΄sα΄ α΄Κα΄ Bα΄α΄**!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("π€ Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("π Refresh / Try Again",
                                                     url=f"https://t.me/{Var.APP_NAME}.herokuapp.com/{usr_cmd}") # Chnage ur app name
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**An error occurred, contact @pyrogrammers group.",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
            
    

    

    


        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"
            
        elif get_msg.photo:
            file_size=f"{get_msg.photo.file_size}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"
        elif get_msg.photo:
            file_name=f"{get_msg.photo.file_name}"

        stream_link = Var.URL + 'watch/' + str(log_msg.message_id) 
        
        online_link = Var.URL + 'download/' + str(log_msg.message_id) 
       

        msg_text ="""
<b>π LINK GENERATED</b>

<b>π€ Name:</b> <u>{}</u>

<b>π― Size:</b> <b>{}</b>

<b>π₯ Download URL: </b> <code>{}</code>"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("πΊ PLAY ONLINE", url=stream_link), #Stream Link
                                                InlineKeyboardButton('π₯ DOWNLOAD NOW', url=online_link)]]) #Download Link
        )


@StreamBot.on_message(filters.regex('helpπ') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**#NEW_USER**\nSomeone started [{message.from_user.first_name}](tg://user?id={message.from_user.id})."
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="You are banned, contact @pyrogrammers group.",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://i.ibb.co/ys3Tgpk/mtzijuhd-0.png",
                Caption="**πΉπΎπΈπ½ πππΏπΏπΎππ πΆππΎππΏ ππΎ πππ΄ α΄ΚΙͺs Bα΄α΄!**\n\n__Dα΄α΄ α΄α΄ Oα΄ α΄ΚΚα΄α΄α΄, OΙ΄ΚΚ CΚα΄Ι΄Ι΄α΄Κ Sα΄Κsα΄ΚΙͺΚα΄Κs α΄α΄Ι΄ α΄sα΄ α΄Κα΄ Bα΄α΄!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("π€ Jα΄ΙͺΙ΄ Uα΄α΄α΄α΄α΄s CΚα΄Ι΄Ι΄α΄Κ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sα΄α΄α΄α΄ΚΙͺΙ΄Ι’ α΄‘α΄Ι΄α΄ WΚα΄Ι΄Ι’. Cα΄Ι΄α΄α΄α΄α΄ α΄α΄__ [ADARSH GOEL](https://t.me/codexmaniachat).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> Send me any file or video i will give you streamable link and download link.</b>\n
<b> I also support Channels, add me to you Channel and send any media files and see miracleβ¨ also send /list to know all commands""",
        parse_mode="HTML",
        disable_web_page_preview=True,
    )
