import os
import threading
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text("مرحبا! البوت راه خدام ✅")

application.add_handler(CommandHandler("start", start))

def process_update(update):
    application.run_polling() # نعالجو في خيط جديد

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    threading.Thread(target=lambda: application.process_update(update)).start()
    return "ok"

@app.route("/")
def home():
    return "ok"
