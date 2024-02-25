from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("lagi gw konekin dulu ke mongo...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("dah konek ke mongo.")
except:
    LOGGER(__name__).error("Gagal Konek Mek, Ke database Mongo lu.")
    exit()
