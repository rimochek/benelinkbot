import asyncio
import logging

from loader import db, dp, bot
from handlers.user import start

async def main():
    logging.basicConfig(
        level=logging.INFO, filename="data/logs.log",
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    
    dp.include_routers(
        start.router
    )

    db.create_tables()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
