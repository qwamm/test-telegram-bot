import telebot, random
TOKEN = "7433098519:AAFSHbiGODBrbpFb51mwrqFD_m1SdPbhS8k"

num = random.randint(1,10)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    num = random.randint(1,10)
    bot.reply_to(message, "Этот бот загадал число от 1 до 10. Вам предлагается угадать, что именно это за число. Введите число, которое, как вы считаете, бот мог загадать.")
def handle_start_help(message):
    bot.reply_to(message, "Вам нужно ввести число от 1 до 10, чтобы попытаться угадать то, что загадал бот.")
@bot.message_handler(regexp = "\D")
def echo_all(message):
    print(message.text)
    bot.reply_to(message, "Введите число")

@bot.message_handler(regexp = "10|[1-9]")
def echo_all(message):
    if num == int(message.text):
        bot.reply_to(message, "Поздравляю, вы угадали)")
    else:
        bot.reply_to(message, "Неверно, попробуйте еще раз")

bot.infinity_polling()