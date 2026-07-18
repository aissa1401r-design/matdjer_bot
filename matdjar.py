import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

application = ApplicationBuilder().token(TOKEN).build()
app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا! البوت راه خدام ✅")

application.add_handler(CommandHandler("start", start))

# نشغلو الابليكاسيون مرة وحدة كي يدماري السيرفر
@app.before_first_request
async def init():
    await application.initialize()
    await application.start()

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok"

@app.route("/")
def home():
    return "Bot is alive"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
