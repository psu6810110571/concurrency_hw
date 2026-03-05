import time
import asyncio
import aiohttp

# เปลี่ยนเป็นเว็บเป้าหมาย และลดเหลือ 10 รอบ
URLS = ["https://www.scrapethissite.com/pages/simple/"] * 10

async def fetch_async(session, url):
    async with session.get(url) as response:
        html_content = await response.text() # ดึงเนื้อหา HTML ของหน้าเว็บ (ต้องมี await)
        return len(html_content)             # คืนค่าเป็น 'จำนวนตัวอักษร'

async def run_asyncio_task():
    print("กำลังเริ่มทำงานแบบ Asyncio (ดึงข้อมูลเว็บจริง)...")
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch_async(session, url)) for url in URLS]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    duration = time.time() - start_time
    
    # ปริ้นโชว์ผลลัพธ์
    print(f"-> โหลดข้อมูลขนาด {results[0]} ตัวอักษร จำนวน {len(URLS)} หน้า")
    print(f"-> Asyncio ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

def run_asyncio():
    # สำหรับ Windows ป้องกัน Error จาก event loop
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run_asyncio_task())

if __name__ == "__main__":
    run_asyncio()