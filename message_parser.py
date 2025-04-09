import asyncio
from telethon import TelegramClient, utils, events
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
session_name = "test"

async def get_chats(client):
    @client.on(events.NewMessage())
    async def handler_all(event):
        chat_id = event.chat_id  # ID чата

        sender_id = event.sender_id  # Получаем ID Юзера
        msg_id = event.id  # Получаем ID сообщения

        sender = await event.get_sender()  # получаем имя юзера
        name = utils.get_display_name(sender)  # Имя Юзера

        chat_from = event.chat if event.chat else (await event.get_chat())  # получаем имя группы
        chat_title = utils.get_display_name(chat_from)  # получаем имя группы

        print(f"ID: {chat_id} {chat_title} >>  (ID: {sender_id})  {name} - (ID: {msg_id}) {event.text}")

    await client.run_until_disconnected()

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    try:
        await get_chats(client)
    finally:
        await client.disconnect()

asyncio.run(main())
