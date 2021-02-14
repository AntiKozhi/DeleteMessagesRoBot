from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import (
    ChatAdminRequired
)

from bot.bot import Bot
from bot.helpers.forward import start_forward

@Bot.on_message(filters.command("forward"))
async def forward(client: Bot, message: Message):
    from_channel = message.text.split(" ",1)[1]
    to_channel = message.chat.id
    await message.reply_text("Starting Forwarding")
    await start_forward(
        client.USER,
        from_channel,
        to_channel,
    )
    await message.reply_text("Completed")