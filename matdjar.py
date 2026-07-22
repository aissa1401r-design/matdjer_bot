import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت خدام 100%")

application.add_handler(CommandHandler("start", start))

@app.post(f"/{TOKEN}")
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    # هاذي تخدم مع 3.10 و 20.7
    application.create_task(application.process_update(update))
    return "ok"

@app.get("/")
def home():
    return "OK"
