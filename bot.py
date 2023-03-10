import telebot

import config

import time

from telebot import types

bot = telebot.TeleBot(config.token)

#   keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Общая информация")
button2 = types.KeyboardButton("Программы обучения")
button3 = types.KeyboardButton("FAQ")
button4 = types.KeyboardButton("Мерч")

markup.add(button1, button2, button3, button4)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте, {0.first_name}. \nЯ <b>{1.first_name}</b>, бот, созданный для помощи вам с поступлением в университет Innopolis!\nВы можете задать мне интересующие вас вопросы или нажать на кнопки в меню. Так же вы можете ввести ключевые слова (бакалавр, магистр, аспирант, грант).".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def phrase(message):
    i = -46
    if message.text == 'Программы обучения':
        message1 = bot.send_message(message.chat.id, "Ищу нужную информацию...")
        time.sleep(1)
        bot.delete_message(message_id=message1.id, chat_id=message.chat.id)
        i -= 1
        bot.send_message(message.chat.id, text= "Наши программы обучения: \n — Бакалавриат: «Информатика и вычислительная техника» и «Анализ данных и искусственный интеллект» \n — Магистратура: «Управление разработкой программного обеспечения», «Робототехника и компьютерное зрение», «Компьютерная безопасность и сети», «Анализ данных и искусственный интеллект» и «Технологическое предпринимательство» \n — Аспирантура: «Теоретические основы информатики» и «Математическое моделирование, численные методы и комплексы программ» \n Подробнее: https://innopolis.university/about/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit")
        i -= 1
    elif message.text == 'Общая информация':
        message1 = bot.send_message(chat_id=message.chat.id, text="Ищу нужную информацию...", )
        time.sleep(1)
        bot.delete_message(message_id=message1.id, chat_id=message.chat.id)
        i -= 1
        bot.send_message(message.chat.id, text= "Университет расположен в городе Иннополис, в 40 км от Казани. Подробнее: https://apply.innopolis.university/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit#?lang=ru&id=12&site=s1&template=university24&landing_mode=edit \n Кампус университета состоит из нескольких корпусов. Студенты проживают в комфортабельных номерах с отдельной кухней и санузлом, оборудованных всей необходимой бытовой техникой и мебелью. На территории кампуса доступен бесплатный Wi-Fi, для студентов работают клининг-сервис и прачечная, есть столовая. Корпуса соединены между собой пешеходной галереей, которая плавно перетекает в здание университета. Большое внимание уделяется безопасности, поэтому на территории жилого комплекса действует пропускной режим. Подробнее: https://innopolis.university/campus?lang=ru&id=12&site=s1&template=university24&landing_mode=edit \n Университет Иннополис предоставляет студентам широкие возможности для самореализации. В вузе работает большое количество творческих и научных клубов, проводятся спортивные и инженерные соревнования.")
        i -= 1
    elif message.text == "FAQ":
        message1 = bot.send_message(message.chat.id,"Секунду...")
        time.sleep(1)
        bot.delete_message(message_id=message1.id, chat_id=message.chat.id)
        i -= 1
        markup3 = types.ReplyKeyboardMarkup(row_width=1)
        askbutton1 = types.InlineKeyboardButton(
            "Какие факультеты (направления подготовки) есть в Университете Иннополис?")
        askbutton3 = types.KeyboardButton("Сколько стоит учеба в Университете Иннополис?")
        askbutton2 = types.KeyboardButton("Как иностранному гражданину поступить в Университет Иннополис?")
        askbutton4 = types.KeyboardButton("Могу ли я обучаться за счет собственных средств?")
        askbutton5 = types.KeyboardButton("Получают ли студенты Университета стипендию?")
        askbutton6 = types.KeyboardButton(
            "Нужно ли сдавать ЕГЭ по английскому языку для поступления на 1 курс бaкалавриата?")
        askbutton7 = types.KeyboardButton("На каком языке нужно предоставить документы?")
        backbutton1 = types.KeyboardButton("Назад")
        askbutton8 = types.KeyboardButton(
            "Есть ли ограничения по возрасту для поступающих на первый курс?")
        markup3.add(askbutton8, askbutton7, askbutton6, askbutton5, askbutton4, askbutton3, askbutton2, askbutton1,
                    backbutton1)
        bot.send_message(message.chat.id, "Вот самые часто задаваемые вопросы.",
                         reply_markup=markup3)
    elif message.text == "Мерч":
        message1 = bot.send_message(message.chat.id, "Ищу нужную информацию...")
        i -= 1
        time.sleep(1)
        bot.delete_message(message_id=message1.id, chat_id=message.chat.id)
        bot.send_message(message.chat.id,
                         "Мерч можно купить по ссылке: https://iustore.innopolis.ru/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit")
        i -= 1
    if message.text == "Назад":
        i -= 1
        time.sleep(1)
        message1 = bot.send_message(message.chat.id, "Возвращаюсь назад...", reply_markup=markup)
        time.sleep(1)
        bot.delete_message(message_id=message1.id, chat_id=message.chat.id)
        i -= 1
        bot.send_message(message.chat.id, "Готово!", reply_markup=markup)
    elif message.text == "Какие факультеты (направления подготовки) есть в Университете Иннополис?":
        i -= 1
        time.sleep(1)
        bot.send_message(message.chat.id,
                         "В 2022-2023 учебном году АНО ВО “Университет Иннополис” осуществляет прием абитуриентов по направлению 09.03.01 “Информатика и вычислительная техника”. По следующим профилям подготовки: \n• Инженерия информационных систем \n• Анализ данных и искусственный интеллект")
    elif message.text == "Сколько стоит учеба в Университете Иннополис?":
        i -= 1
        time.sleep(1)
        bot.send_message(message.chat.id,
                         "Стоимость одного семестра обучения на программе бакалавриата составляет 400 000 рублей. Все кандидаты, успешно прошедшие отбор, получают образовательный грант, покрывающий 100% стоимости обучения или скидку на оплату обучения до 70%.")
        i -= 1
    elif message.text == "Могу ли я обучаться за счет собственных средств?":
        i -= 1
        time.sleep(1)
        bot.send_message(message.chat.id,
                         "Да, в Университете Иннополис можно получить образование на коммерческой основе. Для этого необходимо вовремя подать документы, предъявить результаты ЕГЭ (минимальный балл – 60 по каждому предмету) и внести оплату. Участвовать в грантовом конкурсе Университета Иннополис при этом не обязательно, но рекомендуется.Также есть возможность получить скидку на оплату обучения в размере 70%, 50% или 30% в том случае, если вы успешно прошли грантовый конкурс, но набрали недостаточно баллов на ЕГЭ.")
        i -= 1
    elif message.text == "Получают ли студенты Университета стипендию?":
        i -= 1
        time.sleep(1)
        bot.send_message(message.chat.id,
                         "Студенты Университета Иннополис получают материальную поддержку в виде академической стипендии по результатам сессии. Повышенная стипендия назначается за индивидуальные успехи и особые достижения в учебе, различных олимпиадах и конкурсах. В зависимости от успеваемости стипендия за академические успехи достигает 30000 рублей. Также предусмотрены надбавки за внеучебную активность.")
        i -= 1
    elif message.text == "Нужно ли сдавать ЕГЭ по английскому языку для поступления на 1 курс бaкалавриата?":
        i -= 1
        time.sleep(1)
        bot.send_message(message.chat.id,
                         "Сдавать ЕГЭ по английскому языку для поступления в Университет Иннополис не требуется; результат не влияет на поступление.")
        i -= 1
    elif message.text == "Есть ли ограничения по возрасту для поступающих на первый курс?":
        i -= 1
        time.sleep(1)
        bot.send_message(message.chat.id, "Ограничений по возрасту нет.")
        i -= 1
    elif message.text == "Как иностранному гражданину поступить в Университет Иннополис?":
        i -= 1
        time.sleep(1)
        bot.send_message(message.chat.id,
                         "Иностранные граждане поступают в Университет Иннополис на общих основаниях, по конкурсу на получение гранта. Необходимо заполнить заявку, прикрепить требуемые документы и пройти тесты. Более подробная информация доступна на англоязычной версии сайта.")
        i -= 1
    elif message.text == "На каком языке нужно предоставить документы?":
        i -= 1
        bot.send_message(message.chat.id,
                         "Портфолио/CV, мотивационное письмо и другие документы оформляются на английском языке. Если изначально рекомендательное письмо на русском языке, то необходимо прикрепить на второй странице его перевод. Заверять нотариально ничего не нужно. Сертификаты предоставляются на языке оригинала, перевод предоставляется по требованию.")
    words = message.text

    keywords1 = ["магистр", "магистром", "магистра", "магистратура", "магистратуру", "магистратуре", "Магистр",
                 "Магистром", "Магистра", "Магистратура", "Магистратуру", "Магистратуре"]
    keywords2 = ["бакалавром", "бакалавр", "бакалавра" "бакалавриат", "бакалавриатом", "бакалавриате", "Бакалавром",
                 "Бакалавр", "Бакалавра", "Бакалавриат", "Бакалавриатом"]
    keywords3 = ["аспирант", "аспирантом", "аспиранта", "аспирантура", "аспирантуру", "аспирантуре", "Аспирант",
                 "Аспирантом", "Аспиранта", "Аспирантура", "Аспирантуру", "Аспирантуре"]
    keywords4 = ["грант", "грантом", "гранта", "грантовый", "грантовая", "грантовой", "Грант", "Грантом", "Гранта",
                 "Грантовый", "Грантовая", "Грантовый", "Грантовая", "Грантовой"]
    for keyword in keywords4:
        if keyword in words:
            time.sleep(1)
            bot.send_message(message.chat.id,
                             "Какие размеры грантов действуют в Университете Иннополис? \n 1. 100% грант со стипендией – покрывает полную стоимость обучения и даёт возможность получить стипендию от Университета Иннополис или от компаний-резидентов.\n 2. 100% грант – покрывает полную стоимость обучения и даёт возможность получать стипендию в зависимости от успеваемости. \n 3. Частичный грант - 70%, 50% и 30% включает часть стоимости обучения и возможность получить стипендию в зависимости от успеваемости.")
        else:
            i += 1
    for keyword in keywords3:
        if keyword in words:
            time.sleep(1)
            bot.send_message(message.chat.id,
                             "Вот что я нашёл для вас:https://apply.innopolis.university/postgraduate-study/")
        else:
            i += 1
    for keyword in keywords2:
        if keyword in words:
            time.sleep(1)
            bot.send_message(message.chat.id, "Вот что я нашёл для вас: https://apply.innopolis.university/bachelor/")
        else:
            i += 1
    for keyword in keywords1:
        if keyword in words:
            time.sleep(1)
            bot.send_message(message.chat.id, "Вот что я для вас нашёл: https://apply.innopolis.university/master")
        else:
            i += 1
    if i == 2:
        time.sleep(1)
        bot.send_message(message.chat.id, "Простите, я вас не понял.")


bot.polling(none_stop=True)
# примечание: код работал через компьютер, для полноценной работы загрузите его на хостинг, пожалуйста.
