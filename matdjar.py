import telebot
import os

BOT_TOKEN=os.getenv(BOT_TOKEN)
bot=telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commends=["start"])
def send_welcome(message):
  bot.reply_to(message, "مرجبا بك في متجرك  \nباش تشوف الاوامر اكتب /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "الاوامر المتاحة :  \n بداية - start\n المساعدة - help")

print("bot is running...")
bot.infinity_polling()
  
