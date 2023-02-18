import telebot

import config

from telebot import types

bot = telebot.TeleBot(config.token)

#   keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Общая информация")
button2 = types.KeyboardButton("Для абитуриентов")

markup.add(button1, button2)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте, {0.first_name}. \nЯ <b>{1.first_name}</b>, бот, созданный для помощи вам с поступлением в университет Innopolis!\nВы можете задать мне интересующие вас вопросы.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def phrase(message):
    if message.text == 'Общая информация':
        bot.send_message(message.chat.id,
                         "Наши программы обучения: \n — Бакалавриат: «Информатика и вычислительная техника» и «Анализ данных и искусственный интеллект» \n — Магистратура: «Управление разработкой программного обеспечения», «Робототехника и компьютерное зрение», «Компьютерная безопасность и сети», «Анализ данных и искусственный интеллект» и «Технологическое предпринимательство» \n — Аспирантура: «Теоретические основы информатики» и «Математическое моделирование, численные методы и комплексы программ» \n Подробнее: https://innopolis.university/about/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit")
    elif message.text == 'Для абитуриентов':
        bot.send_message(message.chat.id,
                         "Университет расположен в городе Иннополис, в 40 км от Казани. Подробнее: https://apply.innopolis.university/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit#?lang=ru&id=12&site=s1&template=university24&landing_mode=edit \n Кампус университета состоит из нескольких корпусов. Студенты проживают в комфортабельных номерах с отдельной кухней и санузлом, оборудованных всей необходимой бытовой техникой и мебелью. На территории кампуса доступен бесплатный Wi-Fi, для студентов работают клининг-сервис и прачечная, есть столовая. Корпуса соединены между собой пешеходной галереей, которая плавно перетекает в здание университета. Большое внимание уделяется безопасности, поэтому на территории жилого комплекса действует пропускной режим. Подробнее: https://innopolis.university/campus?lang=ru&id=12&site=s1&template=university24&landing_mode=edit \n Университет Иннополис предоставляет студентам широкие возможности для самореализации. В вузе работает большое количество творческих и научных клубов, проводятся спортивные и инженерные соревнования.")

    words = message.text
    
    word = words.split()

    queries = [1]

    keywords = ["магистр", "магистром", "магистра", "магистратура", "магистратуру", "магистратуре, бакалавром", "бакалавр", "бакалавра" "бакалавриат", "бакалавриатом", "бакалавриате, аспирант", "аспирантом", "аспиранта", "аспирантура", "аспирантуру", "аспирантуре, грант", "грантом", "гранта", "грантовый", "грантовая", "грантовой"]

    for word in words:
        if word in keywords:
            queries.append("Ищу информацию по запросу" + word + "...")


# RUN
bot.polling(none_stop=True)
