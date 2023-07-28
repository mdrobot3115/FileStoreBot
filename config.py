import os

API_ID = int(os.environ.get("API_ID", "9844066"))
API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5681317447:AAHQago7FjR9bXKQrK67lE-Cwr3g9mNgBhI")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1001601351923")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "1445283714"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1001601351923')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
