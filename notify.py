# -*- coding: utf-8 -*-
"""
LichAm - Thong bao ngay mung 1 va ram am lich qua Telegram.
Script chay hang ngay: neu ngay mai la mung 1 hoac 15 am se gui nhac nho.
"""

import sys
import os

# Force UTF-8 output (tranh loi encoding tren Windows terminal)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
import requests
from datetime import date, timedelta
from lunardate import LunarDate


def get_lunar_day(solar_date: date) -> tuple[int, int, int]:
    """Trả về (ngày âm, tháng âm, năm âm) từ ngày dương."""
    lunar = LunarDate.fromSolarDate(solar_date.year, solar_date.month, solar_date.day)
    return lunar.day, lunar.month, lunar.year


def send_telegram(token: str, chat_id: str, message: str) -> bool:
    """Gửi tin nhắn qua Telegram Bot API. Trả về True nếu thành công."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        response = requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": message,
                "parse_mode": "HTML",
            },
            timeout=10,
        )
        response.raise_for_status()
        print("[OK] Da gui Telegram thanh cong.")
        return True
    except requests.RequestException as e:
        print(f"[LOI] Loi gui Telegram: {e}")
        return False


def build_message(lunar_day: int, lunar_month: int, solar_tomorrow: date) -> str | None:
    """
    Tạo nội dung thông báo dựa trên ngày âm lịch của ngày mai.
    Trả về None nếu không cần thông báo.
    """
    solar_str = solar_tomorrow.strftime("%d/%m/%Y")

    if lunar_day == 1:
        return (
            f"🕯️ <b>Nhắc nhở: Ngày mai là Mùng 1 Âm lịch</b>\n"
            f"📅 Mùng 1 tháng {lunar_month} Âm lịch\n"
            f"🗓️ Dương lịch: {solar_str}\n\n"
            f"Nhớ chuẩn bị lễ thắp hương cúng cụ ạ! 🙏"
        )

    if lunar_day == 15:
        return (
            f"🌕 <b>Nhắc nhở: Ngày mai là Rằm (15 Âm lịch)</b>\n"
            f"📅 Rằm tháng {lunar_month} Âm lịch\n"
            f"🗓️ Dương lịch: {solar_str}\n\n"
            f"Nhớ chuẩn bị lễ thắp hương cúng cụ ạ! 🙏"
        )

    return None


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("[LOI] Thieu TELEGRAM_BOT_TOKEN hoac TELEGRAM_CHAT_ID trong bien moi truong.")
        sys.exit(1)

    today = date.today()
    tomorrow = today + timedelta(days=1)

    lunar_day, lunar_month, lunar_year = get_lunar_day(tomorrow)
    print(f"[INFO] Hom nay duong: {today} | Ngay mai am: {lunar_day}/{lunar_month}/{lunar_year}")

    message = build_message(lunar_day, lunar_month, tomorrow)

    if message:
        send_telegram(token, chat_id, message)
    else:
        print(f"[INFO] Ngay mai la ngay {lunar_day} am -> Khong can thong bao.")


if __name__ == "__main__":
    main()
