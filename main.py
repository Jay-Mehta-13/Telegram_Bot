import telebot, os

API_KEY = os.getenv('TELEGRAM_API_KEY')

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['spam'])
def spam(message):
    """ //spam """
    f = open('Text.txt', 'r')
    data = ''
    bot.send_message(message.chat.id, "Hey there, you are about to get spammed", disable_notification=True)
    for line in f:
        # data = data + line
        bot.send_message(message.chat.id, line, disable_notification=True)
    f.close()


@bot.message_handler(commands=['sticker'])
def sticker(message):
    """ //sticker """
    bot.send_sticker(message.chat.id, 'https://img.stickers.cloud/packs/f5bbd6b2-ebaa-4648-b067-a01961250970/webp'
                                      '/a5bf1fd8-f913-483f-9d25-711485f0e737.webp', disable_notification=True)


@bot.message_handler(commands=['topa'])
def topa(message):
    """ //topa """
    bot.send_animation(message.chat.id, 'https://media1.tenor.com/images/02786c93d41e0a6849438b7857f6ac72/tenor.gif'
                                        '?itemid=18744948', disable_notification=True)


@bot.message_handler(commands=['help'])
def help(message):
    """ //help """
    commands = bot.get_my_commands()
    bot.send_message(message.chat.id, commands)


bot.polling()