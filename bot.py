import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    if result.new_chat_member.status == "member":
        user = result.new_chat_member.user
        await context.bot.send_photo(
            chat_id=user.id,
            photo=open("photo.jpg.png", "rb"),
            caption=(
                "Coucou ♥️
Trop cool que tu sois venue sur mon telegram privé !\n\nSi ça te dit je te donne un accès gratuit pour mon OF pour aujourd’hui pour qu’on puisse faire connaissance 😏"
                "https://onlyfans.com/amanda.lpz/c66"
            )
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
app.run_polling(allowed_updates=["chat_member"])
