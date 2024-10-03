
from pyrogram import Client , filters
from pyrogram.types import InlineKeyboardButton as ikb , InlineKeyboardMarkup as ikm
from api import *
import re

bot = Client("mybot", 
    bot_token="6912200154:AAHV5WMXq_KPN752CFVPAkltPi4-3D_HAMU",
    api_id=1712043,
    api_hash="965c994b615e2644670ea106fd31daaf"
)


def check_and_extract_SE(string):
    # Regex pattern to check for the presence of S<number>E<number>
    pattern = r'S(\d+)E(\d+)'
    
    match = re.search(pattern, string)
    
    if match:
        # Extract the integers after S and E
        s_value = int(match.group(1))  # Integer after 'S'
        e_value = int(match.group(2))  # Integer after 'E'
        
        # Remove the matched pattern from the string
        updated_string = re.sub(pattern, '', string).strip()
        
        return True, updated_string, s_value, e_value
    else:
        return False, string, None, None  # Return None for integers if pattern not found

@bot.on_message(filters.command("start"))
async def start_command(bot, message):
    await bot.send_message(message.chat.id , "Send me movie name or series name with its season and episode like 'breaking bad S3E4'")

@bot.on_message(filters.text & filters.private)
async def on_message(bot , message):
    x1 = message.text
    #if check_string_contains_SE(x1) == True:
    #    print('SE working')
    #else:
    #    await bot.send_message(message.chat.id,'Please write season and episode like breaking bad S3E4')
    #    return
    result, updated_string, s_value, e_value = check_and_extract_SE(x1)
    print(result)
    if result:
        print(f'Pattern found and removed: "{updated_string}"\n'
                  f'S value: {s_value}, E value: {e_value}')
    else:
        print(f'Pattern not found, original string: {updated_string}')


    mdetails = search_movie_or_tv(updated_string)
    print(mdetails)
    try:
        id = mdetails['id']
    except:
        await bot.send_message(message.chat.id,'<b>Please enter correct spelling. also make sure you have entered in the correct format.</b>')
    try:
        name = mdetails['title']
    except:
        name = mdetails['name']
    


    if mdetails['type'] =='movie':
        year = mdetails['release_date']
        keyboard = ikm([[ikb('Server 1', url=f'https://moviee.tv/embed/movie/{id}'),ikb('Server 2', url=f'https://vidsrc.me/embed/movie?tmdb={id}')],[ikb('Server 3', url=f'https://player.smashy.stream/movie/{id}')],[ikb('Server 4', url=f'https://moviesapi.club/movie/{id}'),ikb('Server 5', url=f'https://vidlink.pro/movie/{id}')],[ikb('Server 6', url=f'https://player.vidsrc.nl/embed/movie/{id}')]])
        await bot.send_message(message.chat.id,f'<b>Title : {name}. \nRelease Date : {year}.Type : Movie.</b>',reply_markup=keyboard)
    elif mdetails['type'] == 'tv':
        if result == False:
            await bot.send_message(message.chat.id,f'No episode/seasons found in your text, {updated_string}\nPlease mention {updated_string}S4E2 means 4th season and 2nd episode...')
            return
        s = s_value
        e = e_value
        keyboard = ikm([[ikb('Server 1', url=f'https://moviee.tv/embed/tv/{id}?season={s}&episode={e}'),ikb('Server 2', url=f'https://vidsrc.me/embed/tv?tmdb={id}&season={s}&episode={e}')],[ikb('Server 3', url=f'https://player.smashy.stream/tv/{id}?s={s}&e={e}')],[ikb('Server 4', url=f'https://moviesapi.club/tv/{id}-{s}-{e}'),ikb('Server 5', url=f'https://vidlink.pro/tv/{id}/{s}/{e}')],[ikb('Server 6', url=f'https://player.vidsrc.nl/embed/tv/{id}/{s}/{e}')]])
        await bot.send_message(message.chat.id,f'<b>Title : {name}.\nType : TV Show/Web Series.\nSeason : {s} - - Episode : {e}.</b>' ,reply_markup=keyboard)
    else:
        await bot.send_message(message.chat.id,'No results found')
    
        
    #else:
        #await bot.send_message(message.chat.id,'please write season and which episode.')
bot.run()





bot.run()
