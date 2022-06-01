# Developed By : Abhishek Kumar (https://telegram.me/TheTeleRoid) 

import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import *


Bot = Client(
    "Donate",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """Hᴇʏ! {}

☞ Vᴇʀʏ Hᴀᴘᴘʏ ᴛᴏ Kɴᴏᴡ Tʜᴀᴛ Yᴏᴜ ᴀʀᴇ Dᴏɴᴀᴛɪɴɢ Uꜱ.

Tʜᴀɴᴋꜱ Fᴏʀ Uꜱɪɴɢ [Oᴜʀ Bᴏᴛꜱ](https://t.me/+KYLCdC4XfcdmNGVl).

Mᴀᴅᴇ Wɪᴛʜ Lᴏᴠᴇ Fᴏʀ [Yᴏᴜ](tg://settings)"""

DONATE_BUTTONS = [
    InlineKeyboardButton(
        text='Dᴏɴᴀᴛᴇ 💳',
        callback_data='donateme'
    )
]

DONATE_TEXT = """Hᴇʏ! {}
Yᴏᴜ Cᴀɴ Dᴏɴᴀᴛᴇ Uꜱ Uꜱɪɴɢ UPI.

PayTm/PhonePe/GooglePay - `sk7062563@okhdfcbank`

Oʀ Contact Uꜱ :- [Abhishek Kumar](https://telegram.me/HelpLessBoi). """

BUTTON_TEXT = """ Click the Below Buttons To Donate Us. """

UPI_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back ", callback_data="back"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

PAY_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" UPI ", callback_data="upidata"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([DONATE_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["donate"]))
async def filter(bot, update):
    await update.reply_text(
        text="Click the Following Button to Donate Us.",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=" UPI ", callback_data="upidata"),
                 InlineKeyboardButton(text="PayPal", url="https://paypal.me/AbhishekKumarIN47")]
            ],
            [
                [InlineKeyboardButton(text="😥 Close", callback_data="close")]
            ]
        ),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_inline_query()
async def inline_handlers(_, event: InlineQuery):
    answers = list()
    # If Search Query is Empty
    if event.query == "":
        answers.append(
            InlineQueryResultArticle(
                title="This is Inline BotList Search Bot 🔍",
                description="You Can Search All Bots Available On TeleGram.",
                thumb_url="https://telegra.ph/file/330bd070950b8ef775ca9.jpg", 
                input_message_content=InputTextMessageContent(
                    message_text="A dream does not become reality through magic; it takes sweat, determination, and hard work."

",
                    disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Search Here", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("TeleRoid Bots", url="https://t.me/joinchat/t1ko_FOJxhFiOThl"),
                     InlineKeyboardButton("Bots Channel", url="https://t.me/TeleRoidGroup")],
                    [InlineKeyboardButton("TeleGram Bots", url="https://t.me/TGRobot_List")]
                ])
            )
        )

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "donateme":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "upidata":
        await update.message.edit_text(
            text=DONATE_TEXT.format(update.from_user.mention),
            reply_markup=UPI_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "back":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

Bot.run()
