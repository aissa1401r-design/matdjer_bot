import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))
URL = os.environ.get("RENDER_EXTERNAL_URL")

app = Flask(__name__)

# نخدمو الابليكايشن هكا في v20
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="مرحبا ! البوت راه خدام ✅")

application.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update)) # هاذي هي المهمة
    return "ok"

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    # ندير SetWebhook قبل ما نطلع
    asyncio.run(application.bot.set_webhook(url=f"{URL}/{TOKEN}"))
    app.run(host="0.0.0.0", port=PORT)
