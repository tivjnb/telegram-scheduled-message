import asyncio
from telethon import TelegramClient
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
session_name = "test"


async def schedule_message(client, user, message, period, times):
    for i in range(times):
        send_time = datetime.now() + (period*i)
        await client.send_message(user, message, schedule=send_time)
        print(f"Message {i} planed")



async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    user = await client.get_entity("me")
    message = "YOUR MESSAGE HERE"
    period = timedelta(days=0, hours=0, minutes=10)
    n_times_send = 3
    await schedule_message(client, user, message, period, n_times_send)
    await client.disconnect()

asyncio.run(main())
