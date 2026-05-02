import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    if result.new_chat_member.status == "member":
        user = result.new_chat_member.user
        await context.bot.send_message(
            chat_id=user.id,
            text="Coucou 😘\nBienvenue sur mon canal telegram !\n\nTon message ici..."
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
app.run_polling(allowed_updates=["chat_member"])
