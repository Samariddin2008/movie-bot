from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import json
import os
from api_token import token,admin_id 

bot = Bot(token)
dp = Dispatcher()
router = Router()
sponsor_ID = "@taj_movie_see"

# --- Функсияҳои кӯмакчӣ барои файл ---
def load_films():
    if not os.path.exists("film.json"):
        with open("film.json", "w", encoding="utf-8") as f:
            json.dump({}, f)
    with open("film.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_films(films):
    with open("film.json", "w", encoding="utf-8") as f:
        json.dump(films, f, indent=2, ensure_ascii=False)

# --- Барои нигоҳдории ҳолати интизории видео ---
waiting_for_video = {}

async def check_subscription(user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(sponsor_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False


# --- Фармони /start ---
@router.message(Command("start"))
async def start(message: Message):
    if not await check_subscription(message.from_user.id):
        invite_link = f"https://t.me/{sponsor_ID[1:]}"  # тавлиди линк
        await message.answer(
            f"🚫 Барои истифодаи бот, аввал ба канали мо обуна шавед:\n👉 {invite_link}\n\n"
            "Пас аз обуна шудан, /start-ро боз фиристед ✅"
        )
        return

    await message.answer("👋 Салом! Коди филм ё номи онро нависед.")


# --- Фармони /add <код> аз админ ---
@router.message(Command(commands=["add"]))
async def add_command(message: Message):
    if message.from_user.id != admin_id:
        await message.reply("🚫 Танҳо админ метавонад филм илова кунад.")
        return

    args = message.text.split()
    if len(args) != 2:
        await message.reply("Истифода: /add <код> (масалан: /add 56)")
        return

    code = args[1].strip().lower()
    waiting_for_video[message.from_user.id] = code
    await message.reply(f"Лутфан видеои филми рамзи `{code}`-ро фиристед.")

# --- Қабули видео аз админ ва сабт кардани file_id ---
@router.message(lambda msg: msg.content_type == types.ContentType.VIDEO)
async def video_handler(message: Message):
    user_id = message.from_user.id
    if user_id != admin_id:
        await message.reply("🚫 Танҳо админ метавонад видео илова кунад.")
        return

    if user_id not in waiting_for_video:
        await message.reply("Лутфан аввал фармони /add <код> ро фиристед.")
        return

    code = waiting_for_video.pop(user_id)
    file_id = message.video.file_id

    films = load_films()
    films[code] = file_id
    save_films(films)

    await message.reply(f"✅ Видео бо рамзи `{code}` сабт шуд!\nFile ID: `{file_id}`", parse_mode="Markdown")

# --- Фиристодани видео ба корбар ---
@router.message()
async def send_movie(message: Message):
    # 🔹 Қадами 4: пеш аз ҳама — санҷидани обуна
    if not await check_subscription(message.from_user.id):
        invite_link = f"https://t.me/{sponsor_ID[1:]}"
        await message.answer(
            f"🚫 Барои истифодаи бот, аввал ба канали мо обуна шавед:\n👉 {invite_link}"
        )
        return  # агар обуна набошад, кодҳои поён иҷро намешаванд

    # 🔹 Агар обуна шуда бошад — филмро мефиристем
    code = message.text.strip().lower()
    films = load_films()

    if code in films:
        await message.reply("🎬 Лутфан интизор шавед, филм фиристода мешавад...")
        try:
            await bot.send_video(chat_id=message.chat.id, video=films[code])
        except Exception as e:
            await message.reply("❌ Хато ҳангоми фиристодани видео.")
            print(f"Error sending video:", e)
    else:
        await message.reply("😔 Ин филм дар база нест. Ба админ муроҷиат кунед.")


# --- Пайваст кардани router ---
dp.include_router(router)

# --- Оғози бот ---
async def main():
    print("✅ Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
