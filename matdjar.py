import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="مرحبا! البوت راه خدام ✅")

application.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.initialize())
    asyncio.run(application.process_update(update))
    return "ok"

@app.route("/")
def index():
    return "Bot is running"

if __name__ == "__main"__:
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
