from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from info import DS_REACT

@Client.on_message(filters.all)
async def send_reaction(_, message: Message):
    try:
        await message.react(emoji=random.choice(DS_REACT))
        
