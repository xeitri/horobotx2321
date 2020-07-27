import telebot
import time
from telebot import types
import json
from xml.etree import ElementTree as ET
import requests
import os
import sys
import bs4
import sched, time
from DateTime import DateTime
from datetime import datetime
from pytz import timezone
import random
import sqlite3

time = datetime.now(timezone('Asia/Tashkent')).strftime('%d.%m.%y')

bot = telebot.TeleBot('1337227478:AAHTFFjO-L_OREx-jWFY6rpcVkJ0wHYipoY')

                    ########PHOTO##########

aries = "AgACAgIAAxkBAAMaXv49EXaKtIKMmrwBEd7VUuCONesAAiywMRsez_FLUt-qZjVNoQuSduuSLgADAQADAgADeQAD_lEDAAEaBA"
taurus = "AgACAgIAAxkBAAMsXv499Hn4CqxY3qBUuDz WkKHn1EAAjewMRsez_FL5oZSxC-lN9YxFd6TLgADAQADAgADeQAD_UUCAAEaBA"
gemini = "AgACAgIAAxkBAAMgXv49Y_sAAR3C8KdMxnoVsfT4tQ7vAAIwsDEbHs_xS1ZWxa_bLbBKBKK6ki4AAwEAAwIAA3kAA4_mAwABGgQ"
cancer = "AgACAgIAAxkBAAMcXv49LJAB54IMcVVaMYbPkTGHsXwAAi6wMRsez_FL1hBDQcmmfPJG-teTLgADAQADAgADeQADwkYCAAEaBA"
leo =  "AgACAgIAAxkBAAMiXv49gWnZR8IiIR3t46w1313YIWkAAjGwMRsez_FLBkoSoTJafJP4WxWVLgADAQADAgADeQADXhEBAAEaBA"
virgo = "AgACAgIAAxkBAAMuXv49-MAjRRx-pnSmCO5eS8qfCaUAAjiwMRsez_FL_WV6T1BxM7Y0ahiVLgADAQADAgADeQADzBIBAAEaBA"
libra = "AgACAgIAAxkBAAMkXv49lzxv2gwBdVllodlvYcWEGzIAAjOwMRsez_FLfZVEaicvbD8vXPiULgADAQADAgADeQADrHYBAAEaBA"
scorpio = "AgACAgIAAxkBAAMqXv497m-C_zkbso0o6rmH_l38ylcAAjawMRsez_FLG7cODeIYInIEAVGRLgADAQADAgADeQADd3IFAAEaBA"
sagittarius = "AgACAgIAAxkBAAMoXv49zJclbDs9imbv8M_j7ZlVpqcAAjWwMRsez_FLo1jb20l3ShEF8umSLgADAQADAgADeQAD700DAAEaBA"
capricorn = "AgACAgIAAxkBAAMeXv49S_I-fIqcLpbD278fYe-A7HMAAi-wMRsez_FLTapCZ1n38t54O4WSLgADAQADAgADeQADVU8DAAEaBA"
aquarius = "AgACAgIAAxkBAAMYXv486t_vaCXpMRqe9rjFX8GuaKcAAiuwMRsez_FLyccVMUt8O4Bds4OSLgADAQADAgADeQADvkkDAAEaBA"
pisces = "AgACAgIAAxkBAAMmXv49svM7xv8sO__TmSNpzEDfrWEAAjSwMRsez_FLHZm8P68nhsIwGgiSLgADAQADAgADeQADaFIDAAEaBA"

hi = ['🙋‍♂', '🙋🏻‍♂', '🙋🏼‍♂', '🙋🏽‍♂', '🙋🏾‍♂', '🙋🏿‍♂', '🙋‍♀', '🙋🏻‍♀', '🙋🏼‍♀', '🙋🏽‍♀', '🙋🏾‍♀', '🙋🏿‍♀']
serdce = ['❤️', '😻', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤎', '❣️', '💕', '💞', '💓', '💗', '💖', '💘', '💝']
admin = 882979172

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет {0.first_name}'.format(message.chat, bot.get_me()) + random.choice(hi) + '\n/Horoscope - Нажми чтобы узнать свой гороскоп на сегодняшний день',
        parse_mode = 'html')
@bot.message_handler(commands=['getdb'])
def getdb(message):
    if message.from_user.id == admin:
        bot.send_document(admin, open('user.db', 'rb'));
    else:
        print('z')
@bot.message_handler(commands=['Horoscope'])
def inline(message):
    userid = message.chat.id
    firstname = message.chat.first_name
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS users (
        user_id INT NOT NULL,
        user_name TEXT
    )""")
    conn.commit()
    try:
        c.execute("SELECT * FROM users")
        if c.fetchone() is None:
            c.execute("INSERT INTO users (user_id, user_name) VALUES (?, ?);", (userid, firstname))
        else:
            print('Записан')
    except sqlite3.DatabaseError as error:
        print("Error:", error)
    conn.commit()
    conn.close()

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
    request = requests.get("https://orakul.com/horoscope/astrologic/love/aries/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, aries, luv_caption)

@bot.message_handler(commands=['taurus_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/taurus/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, taurus, luv_caption)

@bot.message_handler(commands=['gemini_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/gemini/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, gemini, luv_caption)

@bot.message_handler(commands=['cancer_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/cancer/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, cancer, luv_caption)

@bot.message_handler(commands=['leo_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/leo/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, leo, luv_caption)

@bot.message_handler(commands=['virgo_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/virgo/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, virgo, luv_caption)

@bot.message_handler(commands=['libra_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/libra/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, libra, luv_caption)

@bot.message_handler(commands=['scorpio_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/scorpio/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, scorpio, luv_caption)

@bot.message_handler(commands=['sagittarius_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/sagittarius/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, sagittarius, luv_caption)

@bot.message_handler(commands=['capricorn_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/capricorn/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, capricorn, luv_caption)

@bot.message_handler(commands=['aquarius_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/aquarius/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, aquarius, luv_caption)

@bot.message_handler(commands=['pisces_love'])
def start_message(message):
    request = requests.get("https://orakul.com/horoscope/astrologic/love/pisces/today.html")
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    horoscope_txt = soup.find('div', 'horoBlock').getText()
    luv_caption = horoscope_txt + '\n' + '/Horoscope - Ежедневный гороскоп' + '\n\n' + '@xtr_wallpapers - Подпишитесь на наш канал'
    bot.send_photo(message.chat.id, pisces, luv_caption)







def as_horoscope():
        global as_caption
        request = requests.get("https://horo.mail.ru/prediction/aries/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        as_caption = time + '\n' + horoscope_txt + '\n\n' + '/aries_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def ts_horoscope():
        global ts_caption
        request = requests.get("https://horo.mail.ru/prediction/taurus/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        ts_caption = time + '\n' + horoscope_txt + '\n\n' + '/taurus_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def gi_horoscope():
        global gi_caption
        request = requests.get("https://horo.mail.ru/prediction/gemini/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        gi_caption = time + '\n' + horoscope_txt + '\n\n' + '/gemini_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def cr_horoscope():
        global cr_caption
        request = requests.get("https://horo.mail.ru/prediction/cancer/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        cr_caption = time + '\n' + horoscope_txt + '\n\n' + '/cancer_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def lo_horoscope():
        global lo_caption
        request = requests.get("https://horo.mail.ru/prediction/leo/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        lo_caption = time + '\n' + horoscope_txt + '\n\n' + '/leo_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def vo_horoscope():
        global vo_caption
        request = requests.get("https://horo.mail.ru/prediction/virgo/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        vo_caption = time + '\n' + horoscope_txt + '\n\n' + '/virgo_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def la_horoscope():
        global la_caption
        request = requests.get("https://horo.mail.ru/prediction/libra/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        la_caption = time + '\n' + horoscope_txt + '\n\n' + '/libra_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def so_horoscope():
        global so_caption
        request = requests.get("https://horo.mail.ru/prediction/scorpio/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        so_caption = time + '\n' + horoscope_txt + '\n\n' + '/scorpio_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def ss_horoscope():
        global ss_caption
        request = requests.get("https://horo.mail.ru/prediction/sagittarius/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        ss_caption = time + '\n' + horoscope_txt + '\n\n' + '/sagittarius_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def cn_horoscope():
        global cn_caption
        request = requests.get("https://horo.mail.ru/prediction/capricorn/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        cn_caption = time + '\n' + horoscope_txt + '\n\n' + '/capricorn_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def aqs_horoscope():
        global aqs_caption
        request = requests.get("https://horo.mail.ru/prediction/aquarius/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        aqs_caption = time + '\n' + horoscope_txt + '\n\n' + '/aquarius_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)
def ps_horoscope():
        global ps_caption
        request = requests.get("https://horo.mail.ru/prediction/pisces/today/")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        horoscope_txt = soup.find('div', 'article__item article__item_alignment_left article__item_html').getText()
        ps_caption = time + '\n' + horoscope_txt + '\n\n' + '/pisces_love - Чтобы узнать любовный гороскоп' + random.choice(serdce)

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
