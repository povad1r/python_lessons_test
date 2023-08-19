import asyncpg
import asyncio


class Database():
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                host='ep-old-heart-356850.eu-central-1.aws.neon.tech',
                port='5432',
                database='neondb',
                user='povad1r',
                password='mUlN0H2hIspZ'
            )
        )


    async def register_student(self, name, age, email):
        sql = f"""
        INSERT INTO students (name, age, email) VALUES ({name}, {age}, {email})
        """
        await self.pool.execute(sql)