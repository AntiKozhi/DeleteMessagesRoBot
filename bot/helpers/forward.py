from typing import List
import asyncio
from bot.bot import Bot
from pyrogram.types import Message
async def start_forward(
    client: Bot,
    from_channel,
    to_channel
):
    count = 0
    c = 0
    async for message in client.search_messages(from_channel,filter='document'):
            await asyncio.sleep(3)
            await client.send_message(
                chat_id = to_channel,
                "Hai"
                #from_chat_id = from_channel,
                #message_id = message.message_id
            )
