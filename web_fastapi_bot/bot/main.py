import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN="6892706561:AAFTaxybOdKfN53-XlHDqqorqe_mYVnOn2Q"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Привет, Это бот и я отправляю уведомление!
    Команды:
    /subscribe
    """)

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.chat.username, update.message.chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Поздравляю! Вы подписаны!
    """)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('subscribe', subscribe))
    print("bot started")
    application.run_polling()
    print("bot stopped")



