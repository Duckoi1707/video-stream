# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Chào mừng [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) cho phép bạn phát nhạc và video trên các nhóm thông qua các cuộc trò chuyện video mới của Telegram!**

💡 **Tìm hiểu tất cả các lệnh của Bot và cách chúng hoạt động bằng cách nhấp vào » 📚 Nút lệnh!**

🔖 **Để biết cách sử dụng bot này, vui lòng nhấp vào » ❓ Nút Hướng dẫn Cơ bản!**""",
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
                    InlineKeyboardButton("❤ Quyên tặng", url=f"https://t.me/{OWNER_NAME}"),
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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Hướng dẫn cơ bản để sử dụng bot này:**

1.) **Đầu tiên, hãy thêm tôi vào nhóm của bạn.**
2.) **Sau đó, thăng cấp tôi làm quản trị viên và cấp tất cả các quyền ngoại trừ Quản trị viên ẩn danh.**
3.) **Sau khi quảng cáo cho tôi, hãy nhập /tai trong nhóm để làm mới dữ liệu quản trị.**
3.) **Thêm vào @{ASSISTANT_NAME} vào nhóm của bạn hoặc lệnh /userbotjoin mời cô ấy.**
4.) **Bật trò chuyện video trước khi bắt đầu chơi video/music.**
5.) **Đôi khi, tải lại bot bằng cách sử dụng /tai lệnh có thể giúp bạn khắc phục một số vấn đề.**

📌 **Nếu userbot không tham gia trò chuyện video, hãy đảm bảo rằng trò chuyện video đã được bật hoặc nhập /userbotleave sau đó gõ /userbotjoin lần nữa.**

💡 **Nếu bạn có câu hỏi tiếp theo về bot này, bạn có thể cho biết trên trò chuyện hỗ trợ của tôi tại đây: @{GROUP_SUPPORT}**

⚡ Điều Hành Bởi {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Quay lại", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **xin chào [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **nhấn nút bên dưới để đọc giải thích và xem danh sách các lệnh có sẵn !**

⚡ __Powered bởi {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Quản trị viên Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Thành viên Cmnd", callback_data="cbsudo"),
                ],[
                    
                    InlineKeyboardButton("📚 Căn bản Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Quay lại", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 đây là các lệnh cơ bản:

» /phat (tên bài hát/liên kết) - phát nhạc trên trò chuyện video
» /stream (truy vấn/liên kết) - phát trực tiếp yt live / radio live music
» /phatv (băng hình tên/liên kết) - phát video trên trò chuyện video
» /vstream - phát video trực tiếp từ yt live / m3u8
» /playlist - show you the playlist
» /video (truy vấn) - tải xuống video từ youtube
» /song (truy vấn) - tải bài hát từ youtube
» /lyric (truy vấn) - bỏ lời bài hát
» /search (truy vấn) - tìm kiếm một liên kết video youtube

» /ping - hiển thị trạng thái ping của bot
» /uptime - hiển thị trạng thái thời gian hoạt động của bot
» /thongtin - hiển thị thông tin còn sống của bot (trong nhóm)

⚡️ Bản Quyền bởi {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Quay lại", callback_data="cbcmds")]]
           
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 đây là lệnh quản trị:

» /pause - tạm dừng luồng 
» /resume - tiếp tục luồng
» /skip - chuyển sang luồng tiếp theo
» /tat - dừng phát trực tuyến
» /vmute - tắt tiếng userbot trong cuộc trò chuyện thoại
» /vunmute - bật tiếng người dùng trong cuộc trò chuyện thoại
» /volume `1-200` - điều chỉnh âm lượng của nhạc (userbot phải là quản trị viê)
» /tai - tải lại bot và làm mới dât quản trị
» /userbotjoin - mời userbot tham gia nhóm
» /userbotleave - ra lệnh cho userbot rời khỏi nhóm

⚡️ Bàn Quyền thuộc {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Quay lại", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 đây là các lệnh sudo:

» /rmw - làm sạch tất cả các tệp
» /rmd - dọn dẹp tất cả các tệp đã tải xuống
» /sysinfo - hiển thị thông tin hệ thống
» /update - cập nhật bot của bạn lên phiên bản mới nhất
» /restart - khởi động lại bot của bạn
» /leaveall - ra lệnh cho userbot rời khỏi tất cả nhóm

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Quay lại", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("bạn là quản trị viên ẩn danh !\n\n» hoàn nguyên về tài khoản người dùng từ quyền quản trị.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 chỉ quản trị viên có quyền quản lý cuộc trò chuyện thoại mới có thể nhấn vào nút này!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **cài đặt of** {query.message.chat.title}\n\n⏸ : tạm dừng luồng\n▶️ : \n🔇 : người dùng tắt tiếng\n🔊 : bật tiếng người dùng\n⏹ : dừng dòng",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ hiện không có gì đang phát trực tuyến", show_alert=True)

@Client.on_callback_query(filters.regex("cbtt"))
async def cbtt(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Các Lệnh Cơ Bản Bot:

» /phat - Phát nhạc trực tuyến youtube
» /phatv - Phát nhạc kèm video youtube
» /skip - Bỏ qua bài hát đang phát
» /tai - Để làm mới bot tránh lag 
» /taiv - Để tải video youtube
» /danhs - Để hiện danh sách đang phát
» /thongtin - Để hiện thông tin cập nhật bot

⚡ Bản Quyền Bởi {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Quay lại", callback_data="cls")]]
        ),
    )

@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 chỉ quản trị viên có quyền quản lý cuộc trò chuyện thoại mới có thể nhấn vào nút này !", show_alert=True)
    await query.message.delete()
