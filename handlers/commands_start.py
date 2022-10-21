from aiogram import types
from misc import dp,bot
import asyncio
import random
import datetime
import pytz
from .sqlit import get_caption,reg_user,get_caption2
reg_user(1)
content_id = -1001656498705

link0 = -1001167128067 #Сок
link1 = -1001653876311 #Эстетика
link2 = -1001734017178 #Твои подруги
link3 = -1001716243032 #ПОРНО 24/7
link4 = -1001701960941 #Архивы фуллов
link5 = -1001681795382 #Твои студентки
link6 = -1001518943323 #Домашка
link7 = -1001473420511 #Адская Дрочильня
link8 = -1001706149219

link_c = [link0,link1,link2,link3,link4,link5,link6,link7, link8]
channels = [link0,link1,link2,link3,link4,link5,link6,link7, link8]





async def posting():
    for chaneel in channels:
            try:
                await bot.copy_message(caption = get_caption()[0][0],from_chat_id=content_id,chat_id= chaneel,message_id = random.randint(191,643 - 1), parse_mode='html')
                await bot.copy_message(caption=get_caption2()[0][0], from_chat_id=content_id, chat_id=chaneel,message_id=random.randint(191, 643 - 1), parse_mode='html')
            except Exception as e:
                print(e)
                try:
                    await bot.copy_message(caption=get_caption()[0][0], from_chat_id=content_id, chat_id=chaneel,message_id=random.randint(191, 643 - 1), parse_mode='html')
                    await bot.copy_message(caption=get_caption2()[0][0], from_chat_id=content_id, chat_id=chaneel,message_id=random.randint(191, 643 - 1), parse_mode='html')
                except: pass

    print('Выложил посты во все каналы. Скрипт спит 30 минут')


def second_time(finish_data):
    hours_f = int(finish_data[0:2]) #Часы финиша
    min_f = int(finish_data[3:]) #Минуты финиша
    second_f = 0

    hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour
    min_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).minute
    seconf_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).second


    time_now = datetime.datetime(year = 2022,month = 1,day = 1, hour = hours_now,minute = min_now,second = seconf_now)
    time_finish = datetime.datetime(year = 2022,month = 1,day = 1, hour = hours_f,minute = min_f,second = second_f)

    delta = (time_finish-time_now).seconds
    return delta



async def sender():
    while True:
        await asyncio.sleep(5)
        hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour

        if hours_now == 6 or hours_now == 8 or hours_now == 9 or hours_now == 12 or hours_now == 13 or hours_now == 16 or hours_now == 17 or hours_now == 20:
            if hours_now == 6:
                t = second_time("07:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            if hours_now == 8:
                t = second_time("08:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            if hours_now == 9:
                t = second_time("09:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 12:
                t = second_time("12:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 13:
                t = second_time("13:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 16:
                t = second_time("16:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 17:
                t = second_time("17:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()

            elif hours_now == 20:
                t = second_time("20:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting()


        await asyncio.sleep(1800) #Проверяем каждые 30 минут

