from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("Tuần", 60 * 60 * 24 * 7),
    ("Ngày", 60 * 60 * 24),
    ("Giờ", 60 * 60),
    ("Phút", 60),
    ("Giây", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Chào mừng {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Cho phép bạn phát nhạc và video trên các nhóm thông qua các cuộc trò chuyện video của Telegram mới!**

💡 **Tìm hiểu tất cả các lệnh của Bot và cách chúng hoạt động bằng cách nhấp vào nút Lệnh!**

🔖 **Để biết cách sử dụng bot này, vui lòng nhấp vào » ❓ Hướng dẫn cơ bản!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Thêm tôi vào Nhóm của bạn ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Hướng dẫn cơ bản", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Lệnh", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ Quyên tặng", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Nhóm chính thức", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Kênh chính thức", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["thongtin", f"thongtin@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Nhóm Hỗ Trợ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "Kênh Hỗ Trợ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"Thông Tin Bot Telegram Thế Hệ Thứ 0.5\n\nNgười Thiết Kế : @OGGYVN\nPhiên Bản : 0.2\nCập Nhật Lần Cuối 1/12/2021"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `Tốc Độ Mạng Đo Được!!`\n" f"⚡️ `{delta_ping * 100:.3f} ms`")

    

@Client.on_message(
    command(["lenh", f"lenh@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Nhóm Hỗ Trợ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "Kênh Hỗ Trợ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f""

    await message.reply_photo(
        photo=f"{IMG_4}",
        caption=alive,
        reply_markup=keyboard,
    )

@Client.on_message(command(["time", f"time@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 Bảng Thông Số Bot:\n"
        f"• **Thời Gian Bot Hoạt Động:** `{uptime}`\n"
        f"• **Cập Nhật Lần Cuối Vào:** `{START_TIME_ISO}`"
    )
