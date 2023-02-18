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

    keywords1 = ["магистр", "магистром", "магистра", "магистратура", "магистратуру, магистратуре"]
    keywords2 = ["бакалавром", "бакалавр", "бакалавра" "бакалавриат", "бакалавриатом", "бакалавриате"]
    keywords3 = ["аспирант", "аспирантом", "аспиранта", "аспирантура", "аспирантуру", "аспирантуре"]
    keywords4 = ["грант", "грантом", "гранта", "грантовый", "грантовая", "грантовой"]
    i=1
    for keyword in keywords4:
        if keyword in words:
            bot.send_message(message.chat.id, "Какие размеры грантов действуют в Университете Иннополис? \n 1. 100% грант со стипендией – покрывает полную стоимость обучения и даёт возможность получить стипендию от Университета Иннополис или от компаний-резидентов.\n 2. 100% грант – покрывает полную стоимость обучения и даёт возможность получать стипендию в зависимости от успеваемости. \n 3. Частичный грант - 70%, 50% и 30% включает часть стоимости обучения и возможность получить стипендию в зависимости от успеваемости.")

    for keyword in keywords3:
        if keyword in words:
            bot.send_message(message.chat.id,"Вот что я нашёл для вас:https://apply.innopolis.university/postgraduate-study/")

    for keyword in keywords2:
        if keyword in words:
            bot.send_message(message.chat.id, "Вот что я нашёл для вас: https://apply.innopolis.university/bachelor/")

    for keyword in keywords1:
        if keyword in words:
            bot.send_message(message.chat.id, "Вот что я для вас нашёл: https://apply.innopolis.university/master")
    if i>=0:
        bot.send_message(message.chat.id, "Простите, я вас не понял.")
