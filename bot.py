import telebot
import time
from telebot import types
import json
from xml.etree import ElementTree as ET
import requests
import os
import sched, time
from DateTime import DateTime
from datetime import datetime
from pytz import timezone
import random

time = datetime.now(timezone('Asia/Tashkent')).strftime('%d.%m.%y')

bot = telebot.TeleBot('1292076999:AAGetjUmgBORXlC4-K-lu9d9ipolHsZ2hLA')

                    ########PHOTO##########
aries = "AgACAgIAAxkBAAMaXv49EXaKtIKMmrwBEd7VUuCONesAAiywMRsez_FLUt-qZjVNoQuSduuSLgADAQADAgADeQAD_lEDAAEaBA"
cancer = "AgACAgIAAxkBAAMcXv49LJAB54IMcVVaMYbPkTGHsXwAAi6wMRsez_FL1hBDQcmmfPJG-teTLgADAQADAgADeQADwkYCAAEaBA"
capricorn = "AgACAgIAAxkBAAMeXv49S_I-fIqcLpbD278fYe-A7HMAAi-wMRsez_FLTapCZ1n38t54O4WSLgADAQADAgADeQADVU8DAAEaBA"
gemini = "AgACAgIAAxkBAAMgXv49Y_sAAR3C8KdMxnoVsfT4tQ7vAAIwsDEbHs_xS1ZWxa_bLbBKBKK6ki4AAwEAAwIAA3kAA4_mAwABGgQ"
leo =  "AgACAgIAAxkBAAMiXv49gWnZR8IiIR3t46w1313YIWkAAjGwMRsez_FLBkoSoTJafJP4WxWVLgADAQADAgADeQADXhEBAAEaBA"
libra = "AgACAgIAAxkBAAMkXv49lzxv2gwBdVllodlvYcWEGzIAAjOwMRsez_FLfZVEaicvbD8vXPiULgADAQADAgADeQADrHYBAAEaBA"
aquarius = "AgACAgIAAxkBAAMYXv486t_vaCXpMRqe9rjFX8GuaKcAAiuwMRsez_FLyccVMUt8O4Bds4OSLgADAQADAgADeQADvkkDAAEaBA"
scorpio = "AgACAgIAAxkBAAMqXv497m-C_zkbso0o6rmH_l38ylcAAjawMRsez_FLG7cODeIYInIEAVGRLgADAQADAgADeQADd3IFAAEaBA"
sagittarius = "AgACAgIAAxkBAAMoXv49zJclbDs9imbv8M_j7ZlVpqcAAjWwMRsez_FLo1jb20l3ShEF8umSLgADAQADAgADeQAD700DAAEaBA"
taurus = "AgACAgIAAxkBAAMsXv499Hn4CqxY3qBUuDzwWkKHn1EAAjewMRsez_FL5oZSxC-lN9YxFd6TLgADAQADAgADeQAD_UUCAAEaBA"
virgo = "AgACAgIAAxkBAAMuXv49-MAjRRx-pnSmCO5eS8qfCaUAAjiwMRsez_FL_WV6T1BxM7Y0ahiVLgADAQADAgADeQADzBIBAAEaBA"
pisces = "AgACAgIAAxkBAAMmXv49svM7xv8sO__TmSNpzEDfrWEAAjSwMRsez_FLHZm8P68nhsIwGgiSLgADAQADAgADeQADaFIDAAEaBA"

hi = ['🙋‍♂', '🙋🏻‍♂', '🙋🏼‍♂', '🙋🏽‍♂', '🙋🏾‍♂', '🙋🏿‍♂', '🙋‍♀', '🙋🏻‍♀', '🙋🏼‍♀', '🙋🏽‍♀', '🙋🏾‍♀', '🙋🏿‍♀']
serdce = ['❤️', '😻', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤎', '❣️', '💕', '💞', '💓', '💗', '💖', '💘', '💝']



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет {0.first_name}'.format(message.chat, bot.get_me()) + random.choice(hi) + '\n/Horoscope - Нажми чтобы узнать свой гороскоп на сегодняшний день',
        parse_mode = 'html')


@bot.message_handler(commands=['Horoscope'])
def inline(message):

    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Овен♈️", callback_data="aries")
    but_2 = types.InlineKeyboardButton(text="Телец♉️", callback_data="taurus")
    but_3 = types.InlineKeyboardButton(text="Близнецы♊️", callback_data="gemini")
    but_4 = types.InlineKeyboardButton(text="Рак♋️", callback_data="cancer")
    but_5 = types.InlineKeyboardButton(text="Лев♌️", callback_data="leo")
    but_6 = types.InlineKeyboardButton(text="Дева♍️", callback_data="virgo")
    but_7 = types.InlineKeyboardButton(text="Весы♎️", callback_data="libra")
    but_8 = types.InlineKeyboardButton(text="Скорпион♏️", callback_data="scorpio")
    but_9 = types.InlineKeyboardButton(text="Стрелец♐️", callback_data="sagittarius")
    but_10 = types.InlineKeyboardButton(text="Козерог♑️", callback_data="capricorn")
    but_11 = types.InlineKeyboardButton(text="Водолей♒️", callback_data="aquarius")
    but_12 = types.InlineKeyboardButton(text="Рыбы♓️", callback_data="pisces")

    key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10, but_11, but_12)
    bot.send_message(message.chat.id, 'Выберите свой знак зодиака', reply_markup=key)


@bot.message_handler(commands=['aries_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('aries/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, aries, luv_caption)

@bot.message_handler(commands=['taurus_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('taurus/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, taurus, luv_caption)

@bot.message_handler(commands=['gemini_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('gemini/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, gemini, luv_caption)

@bot.message_handler(commands=['cancer_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('cancer/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, cancer, luv_caption)

@bot.message_handler(commands=['leo_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('leo/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, leo, luv_caption)

@bot.message_handler(commands=['virgo_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('virgo/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, virgo, luv_caption)

@bot.message_handler(commands=['libra_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('libra/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, libra, luv_caption)

@bot.message_handler(commands=['scorpio_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('scorpio/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, scorpio, luv_caption)

@bot.message_handler(commands=['sagittarius_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('sagittarius/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, sagittarius, luv_caption)

@bot.message_handler(commands=['capricorn_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('capricorn/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, capricorn, luv_caption)

@bot.message_handler(commands=['aquarius_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('aquarius/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, aquarius, luv_caption)

@bot.message_handler(commands=['pisces_love'])
def start_message(message):
    response = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml')
    horoscope_name = 'dailylov.xml'
    if os.path.exists(horoscope_name):
        os.remove(horoscope_name)
    with open(horoscope_name, 'wb') as file:
        file.write(response.content)
    print('Downloaded dailylovvv')
    advice = ET.parse('dailylov.xml')
    text = advice.find('pisces/today').text
    luv_caption = ' '.join(text.split()) + '\n\n' + '/Horoscope - Ежедневный гороскоп'
    bot.send_photo(message.chat.id, pisces, luv_caption)







def as_horoscope():
        global as_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('aries/today').text
        as_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/aries_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def ts_horoscope():
        global ts_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('taurus/today').text
        ts_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/taurus_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def gi_horoscope():
        global gi_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('gemini/today').text
        gi_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/gemini_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def cr_horoscope():
        global cr_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('cancer/today').text
        cr_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/cancer_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def lo_horoscope():
        global lo_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('leo/today').text
        lo_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/leo_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def vo_horoscope():
        global vo_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('virgo/today').text
        vo_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/virgo_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def la_horoscope():
        global la_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('libra/today').text
        la_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/libra_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def so_horoscope():
        global so_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('scorpio/today').text
        so_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/scorpio_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def ss_horoscope():
        global ss_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('sagittarius/today').text
        ss_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/sagittarius_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def cn_horoscope():
        global cn_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('capricorn/today').text
        cn_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/capricorn_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def aqs_horoscope():
        global aqs_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('aquarius/today').text
        aqs_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/aquarius_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def ps_horoscope():
        global ps_caption
        response = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
        horoscope_name = 'daily.xml'
        if os.path.exists(horoscope_name):
            os.remove(horoscope_name)
        with open(horoscope_name, 'wb') as file:
            file.write(response.content)
        print('Downloaded daily')
        advice = ET.parse('daily.xml')
        text = advice.find('pisces/today').text
        ps_caption = time + '\n' + ' '.join(text.split()) + '\n\n' + '/pisces_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'aries':
        as_horoscope()
        bot.send_photo(c.message.chat.id, aries, as_caption)

    if c.data == 'taurus':
        ts_horoscope()
        bot.send_photo(c.message.chat.id, taurus, ts_caption)

    if c.data == 'gemini':
        gi_horoscope()
        bot.send_photo(c.message.chat.id, gemini, gi_caption)

    if c.data == 'cancer':
        cr_horoscope()
        bot.send_photo(c.message.chat.id, cancer, cr_caption)

    if c.data == 'leo':
        lo_horoscope()
        bot.send_photo(c.message.chat.id, leo, lo_caption)

    if c.data == 'virgo':
        vo_horoscope()
        bot.send_photo(c.message.chat.id, virgo, vo_caption)

    if c.data == 'libra':
        la_horoscope()
        bot.send_photo(c.message.chat.id, libra, la_caption)

    if c.data == 'scorpio':
        so_horoscope()
        bot.send_photo(c.message.chat.id, scorpio, so_caption)

    if c.data == 'sagittarius':
        ss_horoscope()
        bot.send_photo(c.message.chat.id, sagittarius, ss_caption)

    if c.data == 'capricorn':
        cn_horoscope()
        bot.send_photo(c.message.chat.id, capricorn, cn_caption)

    if c.data == 'aquarius':
        aqs_horoscope()
        bot.send_photo(c.message.chat.id, aquarius, aqs_caption)

    if c.data == 'pisces':
        ps_horoscope()
        bot.send_photo(c.message.chat.id, pisces, ps_caption)

bot.polling(none_stop=True)
