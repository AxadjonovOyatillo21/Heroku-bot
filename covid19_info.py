import telebot
 # connect all modules
from telebot import types
import config
import covid19cases as covid

# connect bot to code
bot = telebot.TeleBot('1460460364:AAF9iFRy0Rms_EzCTEsJXLg8ouXrVkFhIoM')


# check command start
@bot.message_handler(commands=['start'])
def send_welcome(message):
# send sticker
    sticker = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    hello_text = "Salom, {0}!\n{1} botiga xush kelibsiz!\nSo'ngi ma'lumotlarni olish uchun davlatni tanlang".format(message.from_user.first_name, bot.get_me().first_name)

# make keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtna = types.KeyboardButton('Aqsh')
    itembtnr = types.KeyboardButton('Rossiya')
    itembtnx = types.KeyboardButton('Xitoy')
    itembtni = types.KeyboardButton('Ispaniya')
    itembtnit = types.KeyboardButton('Italiya')
    itembtnu = types.KeyboardButton('O\'zbekiston')
    itembtnt = types.KeyboardButton('Turkiya')
    itembtnhin = types.KeyboardButton('Hindiston')
    markup.row(itembtna, itembtnx, itembtnr, itembtni)
    markup.row(itembtnt, itembtnit, itembtnu)
    bot.send_message(message.chat.id, hello_text, reply_markup=markup)

# check contetn
@bot.message_handler(content_types=["text"])
def get_information(message):
    if message.chat.type == 'private':
    	# check which button selected user
        if message.text == 'Aqsh':
            res = covid.get_country_cases("USA")
        elif message.text == 'Hindiston':
            res = covid.get_country_cases("India")    
        elif message.text == 'Ispaniya':
            res = covid.get_country_cases("Spain")
        elif message.text == 'Rossiya':
            res = covid.get_country_cases("Russia")
        elif message.text == 'O\'zbekiston':
            res = covid.get_country_cases("Uzbekistan")
        elif message.text == 'Buyuk Britaniya':
            res = covid.get_country_cases("UK")
        elif message.text == 'Italiya':
            res = covid.get_country_cases("Italy")
        elif message.text == 'Fransiya':
            res = covid.get_country_cases("France")
        elif message.text == 'Germaniya':
            res = covid.get_country_cases("Germany")
        elif message.text == 'Turkiya':
            res = covid.get_country_cases("Turkey")
        elif message.text == 'Xitoy':
            res = covid.get_country_cases("China")
            
        else:
            res = covid.get_global_cases()


		#send user all text with information
        lat = res['TotalCases']
        new = res['NewCases']
        deth = res['TotalDeaths']
        rec = res['TotalRecovered']
        text = "Jami kasallanganlar soni: {0}\nBugun aniqlangan bemorlar soni: {1}\nJami o'limlar soni: {2}\nJami tuzalganlar soni: {3}\nAgarda bu sonlar ortishini istamasangiz <b>Uyda qoling</b>".format(lat, new.replace("+", ""), deth, rec)
        bot.send_message(message.chat.id, text, parse_mode='html')


# run programm non-stop
bot.polling(none_stop=True)