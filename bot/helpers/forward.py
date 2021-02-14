from typing import List
import asyncio
from bot.bot import Bot

async def start_forward(
    client: Bot,
    from_channel,
    to_channel
):
    count = 0
    c = 0
    async for msg in client.iter_history(
        chat_id=from_channel,
        limit=None
    ):
        if count > 200:
            await asyncio.sleep(200)
            count = 0
        if c == 10000:
            await asyncio.sleep(10800)
        if msg.document:
            doc_id = msg.document.file_id
            caption = msg.caption
            
            await client.send_document(
                chat_id = to_channel,
                document = doc_id,
                caption = caption
            )
            count = count + 1
            c = c + 1
            await asyncio.sleep(3)
        
