# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Heelo")

@BotzHub.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
