import telebot

import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте, {0.first_name}. \nЯ <b>{1.first_name}</b>, бот, созданный для помощи вам с поступлением в университет Innopolis!\nВы можете задать мне интересующие вас вопросы.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')


# RUN
bot.polling(none_stop=True)
