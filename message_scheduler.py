import asyncio
from telethon import TelegramClient
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

from schedule_config import ScheduleConfig

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
session_name = "test"


async def send_scheduled_message(client, user, message ,send_time):
    await client.send_message(user, message, schedule=send_time)

async def schedule_message(client, receiver, message, firs_send_time, period, n_times_send):
    user = await client.get_entity(receiver)
    for i in range(n_times_send):
        send_time = firs_send_time + (period*i)
        await send_scheduled_message(client, user, message, send_time)
        print(f"Message {i} planed")



async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    await schedule_message(client, **config.to_dict())
    await client.disconnect()

if __name__ == '__main__':
    config = ScheduleConfig(
        message="""
        С добрым утром!!!
        """,
        receiver="me",
        firs_send_time=datetime.now() + timedelta(hours=1),
        period=timedelta(
            days=0,
            hours=1,
            minutes=0,
        ),
        n_times_send=5
    )
    asyncio.run(main())
