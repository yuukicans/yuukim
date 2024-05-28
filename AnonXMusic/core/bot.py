from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="ʙᴇʀʟɪɴ✘ʀᴏʙᴏᴛ",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.-1002227326940,
                text=f"<u><b>» ʙʟᴀᴄᴋ ᴀɴɢᴇʟs ᴍᴜsɪᴄ + ᴍᴀɴᴀɢᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴍᴇᴋ! 🔥",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "ʙᴏᴛ ɢᴀɢᴀʟ ᴀᴄᴄᴇs ʟᴏɢ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ. ʟᴜ ᴛᴀᴍʙᴀʜɪɴ ᴅᴜʟᴜ ʙᴏᴛ ᴋᴇ ʟᴏɢ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ʟᴜ."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"ʙᴏᴛ ɢᴀɢᴀʟ ᴀᴄᴄᴇs ʟᴏɢ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.\n  Reason : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.-1002227326940, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "ᴀᴅᴍɪɴɪɴ ᴅᴜʟᴜ ɴɢᴇɴᴛᴏᴛ ʙᴏᴛ ɴʏᴀ ᴅɪ ʟᴏɢ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ʟᴜ."
            )
            exit()
        LOGGER(__name__).info(f"ᴀssɪsᴛᴀɴᴛ ᴍᴜsɪᴄ ʙᴇʀʟɪɴ sᴛᴀʀᴛᴇᴅ ᴀs{self.name}")

    async def stop(self):
        await super().stop()
