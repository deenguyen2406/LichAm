# 🕯️ LichAm - Nhắc nhở thắp hương Mùng 1 & Rằm

Tự động gửi thông báo Telegram trước ngày Mùng 1 và Rằm âm lịch.

## ⚙️ Cách hoạt động

- Chạy mỗi ngày lúc **7:00 sáng (giờ Việt Nam)** qua GitHub Actions
- Nếu ngày mai là **Mùng 1** hoặc **Rằm (15) âm lịch** → gửi tin nhắn Telegram nhắc nhở
- **Không cần server**, hoàn toàn miễn phí

## 🚀 Hướng dẫn cài đặt

### Bước 1: Tạo Telegram Bot

1. Mở Telegram, nhắn `/newbot` cho **@BotFather**
2. Đặt tên và username cho bot → nhận **Bot Token**
3. Nhắn tin cho bot của bạn một lần (để bot biết chat ID)
4. Lấy Chat ID bằng cách truy cập:
   ```
   https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
   ```
   Tìm giá trị `"id"` trong phần `"chat"`

### Bước 2: Thêm Secrets vào GitHub

Vào **Settings → Secrets and variables → Actions → New repository secret**:

| Secret Name | Giá trị |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Token từ BotFather |
| `TELEGRAM_CHAT_ID` | Chat ID của bạn |

### Bước 3: Push code lên GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<username>/LichAm.git
git push -u origin main
```

GitHub Actions sẽ tự động kích hoạt theo lịch đã cấu hình.

## 🧪 Test thủ công

Vào tab **Actions** trên GitHub → chọn workflow **Lunar Calendar Notification** → nhấn **Run workflow**.

## 📁 Cấu trúc project

```
LichAm/
├── .github/
│   └── workflows/
│       └── notify.yml    # Cron job config
├── notify.py             # Script chính
├── requirements.txt      # Dependencies
└── README.md
```

## 📩 Mẫu tin nhắn Telegram

**Trước Mùng 1:**
> 🕯️ **Nhắc nhở: Ngày mai là Mùng 1 Âm lịch**
> 📅 Mùng 1 tháng 3 Âm lịch
> 🗓️ Dương lịch: 27/03/2026
> Nhớ chuẩn bị lễ thắp hương cúng cụ ạ! 🙏

**Trước Rằm:**
> 🌕 **Nhắc nhở: Ngày mai là Rằm (15 Âm lịch)**
> 📅 Rằm tháng 3 Âm lịch
> 🗓️ Dương lịch: 11/04/2026
> Nhớ chuẩn bị lễ thắp hương cúng cụ ạ! 🙏
