# 🎬 Telegram Movie Bot

Ин лоиҳа Telegram бот мебошад, ки бо истифода аз **Python** ва китобхонаи **Aiogram** сохта шудааст.

Бот барои фиристодани филмҳо бо рамз (код) истифода мешавад.  
Корбар кодро мефиристад ва бот филмро мефиристад.

---

## 🚀 Имкониятҳо

- Санҷиши обуна ба канал
- Фиристодани филм бо рамз
- Илова кардани филм аз тарафи админ
- Нигоҳдории филмҳо дар `JSON`
- Сабти автоматии `file_id`
- Муҳофизат аз истифодаи ғайриобунашуда

---

# 📂 Сохтори лоиҳа

```bash
movie_bot/
│── bot.py
│── api_token.py
│── film.json
```

---

# 📌 api_token.py

Дар ин файл токени бот ва ID-и админ нигоҳ дошта мешавад.

```python
token = "YOUR_BOT_TOKEN"
admin_id = 123456789
```

---

# 📌 film.json

Ин файл базаи филмҳоро нигоҳ медорад.

Мисол:

```json
{
  "56": "BAACAgIAAxkBAA..."
}
```

- **Калид** → рамзи филм
- **Арзиш** → file_id-и видео

---

# 📌 bot.py

Файли асосии бот.

---

# 🤖 Импортҳо

```python
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import json
import os
```

Барои коркарди бот ва файлҳо истифода мешавад.

---

# ⚙️ Танзими бот

```python
bot = Bot(token)
dp = Dispatcher()
router = Router()
```

Ин қисм ботро фаъол мекунад.

---

# 📢 Канали ҳатмии обуна

```python
sponsor_ID = "@taj_movie_see"
```

Корбар бояд ба ин канал обуна шавад.

---

# 💾 Боркунии филмҳо

```python
load_films()
```

Филмҳоро аз `film.json` мехонад.

Агар файл набошад → месозад.

---

# 💾 Сабти филмҳо

```python
save_films(films)
```

Маълумотро дар `film.json` сабт мекунад.

---

# ✅ Санҷиши обуна

```python
check_subscription(user_id)
```

Месанҷад, ки корбар ба канал обуна ҳаст ё не.

Агар обуна набошад:

```python
🚫 Барои истифодаи бот, аввал ба канал обуна шавед
```

---

# ▶️ Фармони /start

```python
/start
```

Агар корбар обуна бошад:

```python
👋 Салом! Коди филм ё номи онро нависед.
```

---

# ➕ Илова кардани филм

Танҳо админ метавонад истифода барад:

```python
/add 56
```

Баъд бот мегӯяд:

```python
Лутфан видеоро фиристед
```

Пас аз фиристодани видео:

```python
✅ Видео сабт шуд
```

---

# 🎥 Қабули видео

Бот `file_id`-ро гирифта дар база нигоҳ медорад:

```python
file_id = message.video.file_id
```

---

# 📤 Фиристодани филм

Корбар рамз мефиристад:

```python
56
```

Агар филм бошад:

```python
🎬 Лутфан интизор шавед...
```

ва бот филмро мефиристад.

---

# ❌ Агар филм набошад

```python
😔 Ин филм дар база нест
```

---

# ▶️ Оғози бот

```python
async def main():
    await dp.start_polling(bot)
```

Бот пайваста кор мекунад.

---

# 🛠 Насб

## 1. Клон кардани лоиҳа

```bash
git clone https://github.com/username/movie_bot.git
```

## 2. Даромадан ба папка

```bash
cd movie_bot
```

## 3. Насби китобхонаҳо

```bash
pip install aiogram
```

## 4. Иҷро

```bash
python bot.py
```

---

# 📌 Фармонҳо

### Барои корбар:

```bash
/start
<рамзи филм>
```

### Барои админ:

```bash
/add <код>
```

Мисол:

```bash
/add 56
```

---

# 🧠 Технологияҳо

- Python
- Aiogram
- JSON
- Asyncio
- Telegram Bot API

---

# 👨‍💻 Муаллиф

**Akram Usmon**

Telegram Movie Bot барои идоракунии автоматии филмҳо дар Telegram.
