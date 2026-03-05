import time
import asyncio
import aiohttp

URLS = ["http://olympus.realpython.org/dice"] * 50

async def fetch_async(session, url):
    async with session.get(url) as response:
        return response.status

async def run_asyncio_task():
    print("กำลังเริ่มทำงานแบบ Asyncio (I/O Bound)...")
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch_async(session, url)) for url in URLS]
        await asyncio.gather(*tasks, return_exceptions=True)
    duration = time.time() - start_time
    print(f"-> Asyncio ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

def run_asyncio():
    asyncio.run(run_asyncio_task())

if __name__ == "__main__":
    run_asyncio()