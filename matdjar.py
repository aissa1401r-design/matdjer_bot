import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application,CommandHandler, ContextTypes

app=Flask(__name__)
@app.route('/')
def home():
    return "Matdjar bot is running..."

def run_web():
    app.run(host='0.0.0.0', port=10000)

BOT_TOKEN=os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا, البوت في الخدمة")

def main():
    threading.Thread(target=run_web).start()


    application= Application.builder().token(BOT_TOKEN).build()
    application.add_handler(commandHandler("start",start))
    application.run_polling()

if name == (__main__):
    main()
  
