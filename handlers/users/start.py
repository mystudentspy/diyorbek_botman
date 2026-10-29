from aiogram import Router, filters, types, Bot
rt = Router()
@rt.message(filters.Command("start"))
async def start(msg: types.Message, bot: Bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    await msg.answer(str(user.status))
    await msg.answer("xush kelibsiz, xurmatli foydalanuvchi")

