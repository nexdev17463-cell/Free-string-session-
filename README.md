# ⚡ NEXUS String Generator Bot

A professional Telegram String Session Generator Bot with rich UI, supporting **Pyrogram v2** and **Telethon** (user & bot sessions).

---

## ✦ Features
- Pyrogram v2 — User & Bot sessions
- Telethon — User & Bot sessions
- OTP + 2FA support
- Force-join channel guard
- MongoDB user tracking
- Styled, rich Telegram messages
- GitHub Actions deploy workflow

---

## ✦ GitHub Actions Setup

### 1 · Fork / Clone this repo

### 2 · Add Repository Secrets
Go to `Settings → Secrets and variables → Actions → New repository secret`

| Secret Name   | Description                          |
|--------------|--------------------------------------|
| `API_ID`      | From [my.telegram.org](https://my.telegram.org) |
| `API_HASH`    | From [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN`   | From [@BotFather](https://t.me/BotFather) |
| `OWNER_ID`    | Your Telegram numeric ID             |
| `MONGO_DB_URI`| MongoDB Atlas connection string      |
| `MUST_JOIN`   | Channel username without `@` (optional) |

### 3 · Deploy
- Push to `main` → workflow starts automatically
- Or go to **Actions tab → Run workflow** manually

---

## ✦ Local Setup

```bash
git clone <repo>
cd STRING_BOT
cp sample.env .env
# fill in .env values
pip install -r requirements.txt
python main.py
```

---

## ✦ Commands
| Command | Description |
|---------|-------------|
| `/start` | Welcome message |
| `/generate` or `/gen` or `/string` | Generate a session |
| `/stats` | Owner only — total users |
| `/cancel` | Cancel ongoing generation |
| `/skip` | Use bot's default API keys |
