import time
import asyncio
import concurrent.futures
import requests
import aiohttp

# ==========================================
# ส่วนที่ 1: งาน I/O Bound (เหมาะกับ Threading และ Asyncio)
# ==========================================
URLS = ["http://olympus.realpython.org/dice"] * 50

# 1.1 แบบ Threading
def fetch_url(url):
    response = requests.get(url)
    return response.status_code

def run_threading():
    print("กำลังเริ่มทำงานแบบ Threading (I/O Bound)...")
    start_time = time.time()
    # ใช้ ThreadPoolExecutor เพื่อสร้าง Thread ช่วยกันดึงข้อมูล
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(fetch_url, URLS)
    duration = time.time() - start_time
    print(f"-> Threading ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

# 1.2 แบบ Asyncio
async def fetch_async(session, url):
    async with session.get(url) as response:
        return response.status

async def run_asyncio():
    print("กำลังเริ่มทำงานแบบ Asyncio (I/O Bound)...")
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch_async(session, url)) for url in URLS]
        await asyncio.gather(*tasks, return_exceptions=True)
    duration = time.time() - start_time
    print(f"-> Asyncio ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")


# ==========================================
# ส่วนที่ 2: งาน CPU Bound (เหมาะกับ Process Pool)
# ==========================================
# ฟังก์ชันคำนวณเลขหนักๆ
def calculate(limit):
    return sum(i * i for i in range(limit))

def run_process_pool():
    print("กำลังเริ่มทำงานแบบ Process Pool (CPU Bound)...")
    numbers = [5_000_000 + x for x in range(10)]
    start_time = time.time()
    # ใช้ ProcessPoolExecutor เพื่อกระจายงานคำนวณไปยัง CPU หลายๆ คอร์
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(calculate, numbers)
    duration = time.time() - start_time
    print(f"-> Process Pool ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")


# ==========================================
# จุดเริ่มต้นการรันโปรแกรม
# ==========================================
if __name__ == "__main__":
    print("--- เริ่มการทดสอบโปรแกรม Concurrency ---\n")
    
    # รัน Threading
    run_threading()
    
    # รัน Asyncio (ต้องรันผ่าน asyncio.run)
    asyncio.run(run_asyncio())
    
    # รัน Process Pool (Multiprocessing)
    run_process_pool()
    
    print("--- จบการทดสอบ ---")