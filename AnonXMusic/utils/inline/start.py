from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/InfoMusicCalvin"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=f"https://t.me/UcalMeVin"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], url=f"https://t.me/+ELpTEshSADM1ODc1"),
            InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/+Gok7Kc6Q5SA5NTQ1"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=f"https://t.me/+E3M5iLoVahUyYjY1"),
            InlineKeyboardButton(text=_["S_B_7"], url=f"https://t.me/+-QStFZhEeUk0MDA1"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_8"], url=f"12345678"),
            InlineKeyboardButton(text=_["S_B_9"], url=f"https://t.me/InfoMusicCalvin"),
        ],
    ]
    return buttons
