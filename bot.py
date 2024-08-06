from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as ikb , InlineKeyboardMarkup as ikm


bot = Client('BotServer2',api_id=1712043,
    api_hash="965c994b615e2644670ea106fd31daaf",
    bot_token='6634907060:AAG7-WcGVElolHfIcU8-rnLlFr90efKqb8o')

@bot.on_message(filters.command('start'))
async def start(bot, message):
    buttons = [
        [ikb("Get New ID On WhatsApp", url="https://wa.link/mahaveer_book_official")],
        [ikb("Create ID On Automatic Site", url="https://mahaveerexch.com")],
        [ikb("Join Our Official Telegram Channel", url="https://t.me/+3MWySnnLWC0xYTFl")],
        [ikb("Join Our Official Instagram Page", url="https://instagram.com/mahaveerbook_official?igshid=MzRlODBiNWFlZA==")]],
    await bot.send_photo(message.chat.id, 'https://postimg.cc/SXQDjWF5',caption='<b><i>💰WELCOME TO MAHAVEER EXCHANGE💰</b></i>')
    #await bot.send_message(message.chat.id,'<b><i>💰WELCOME TO MAHAVEER EXCHANGE💰</b></i>')
    await bot.send_message(message.chat.id,'<b>Please click the button below</b>',reply_markup =ikm(buttons))



bot.run()
