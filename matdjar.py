import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

application = ApplicationBuilder().token(TOKEN).build()
app = Flask(name)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا! البوت راه خدام ✅")

application.add_handler(CommandHandler("start", start))


@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():  # <-- درناها async
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    await application.initialize()  # <-- نديرو initialize في كل مرة
    await application.process_update(update)
    return "ok"

@app.route("/")
def home():
    return "Bot is alive"

if name == "main":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
