from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Go Back", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 Close", callback_data="cls")]]
)


@Client.on_message(command(["tai", f"tai@{BOT_USERNAME}", "reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ Bot **tải lại một cách chính xác !**\n✅ **Danh sách quản trị viên** đã được **cập nhật !**"
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "boqua", f"boqua@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Tùy Chỉnh", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="Tạm Đóng", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ không có gì hiện đang chơi")
        elif op == 1:
            await m.reply("✅ __Queues__ **trống rỗng.**\n\n**• userbot rời khỏi cuộc trò chuyện thoại**")
        elif op == 2:
            await m.reply("🗑️ **Xóa hàng đợi**\n\n**• userbot đã chuyển tới bài tiếp theo**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **Đã bỏ qua bài hát tiếp theo.**\n\n🏷 **Tên:** [{op[0]}]({op[1]})\n💭 **Trò chuyện:** `{chat_id}`\n💡 **Trạng thái:** `Playing`\n🎧 **Yêu cầu bởi:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **bài hát bị xóa khỏi hàng đợi:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "tat", f"tat@{BOT_USERNAME}", "vstop"])
    & other_filters
)
Uauthorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ **phát trực tuyến đã kết thúc.**")
        except Exception as e:
            await m.reply(f"🚫 **lỗi:**\n\n`{e}`")
    else:
        await m.reply("❌ **không có gì trong phát trực tuyến**")


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "tamdung", f"tamdumg@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **Theo dõi bị tạm dừng.**\n\n• **Để tiếp tục luồng, hãy sử dụng**\n» /resume chỉ huy."
            )
        except Exception as e:
            await m.reply(f"🚫 **lỗi:**\n\n`{e}`")
    else:
        await m.reply("❌ **không có gì trong phát trực tuyến**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "tieptuc", f"tieptuc@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **Đã tiếp tục theo dõi.**\n\n• **Để tạm dừng luồng, hãy sử dụng**\n» /pause chỉ huy."
            )
        except Exception as e:
            await m.reply(f"🚫 **lỗi:**\n\n`{e}`")
    else:
        await m.reply("❌ **không có gì trong phát trực tuyến**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **Userbot bị tắt tiếng.**\n\n• **Để bật tiếng người dùng, hãy sử dụng**\n» /unmute chỉ huy."
            )
        except Exception as e:
            await m.reply(f"🚫 **lỗi:**\n\n`{e}`")
    else:
        await m.reply("❌ **không có gì trong phát trực tuyến**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **Người dùng đã bật tiếng.**\n\n• **Nếu .muốn tắt  tiếng người dùng, hãy sử dụng**\n» /mute command."
            )
        except Exception as e:
            await m.reply(f"🚫 **lỗi:**\n\n`{e}`")
    else:
        await m.reply("❌ **không có gì trong phát trực tuyến**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ the streaming has paused", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ the streaming has resumed", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **this streaming has ended**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 userbot succesfully muted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 userbot succesfully unmuted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **âm lượng được đặt thành** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **không có gì trong phát trực tuyến**")
