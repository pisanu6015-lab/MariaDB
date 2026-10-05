import os
import mariadb
from dotenv import load_dotenv

# โหลดตัวแปรจากไฟล์ .env
load_dotenv(override=True)

def get_connection():
    db_host = os.getenv("DB_HOST", "127.0.0.1")
    # หากค่าดึงมาได้เป็น localhost ให้เปลี่ยนเป็น 127.0.0.1 ทันที
    if db_host == "localhost":
        db_host = "127.0.0.1"

    return mariadb.connect(
        host=db_host,
        port=int(os.getenv("DB_PORT", 3333)),
        user=os.getenv("DB_USER", "happyuser"),
        password=os.getenv("DB_PASSWORD", "happypassword"),
        database=os.getenv("DB_NAME", "happy_paws"),
    )