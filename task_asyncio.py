import time
import asyncio
import aiohttp
import sys
from bs4 import BeautifulSoup

# ดึงข้อมูล 5 รอบ
URLS = ["https://www.scrapethissite.com/pages/simple/"] * 5

async def fetch_async(session, url):
    async with session.get(url) as response:
        html_content = await response.text()
        soup = BeautifulSoup(html_content, 'html.parser')
        countries = soup.find_all('div', class_='country')
        
        for country in countries:
            name = country.find('h3', class_='country-name').text.strip()
            if name == "Andorra":
                capital = country.find('span', class_='country-capital').text.strip()
                population = country.find('span', class_='country-population').text.strip()
                area = country.find('span', class_='country-area').text.strip()
                
                return f"เจอแล้ว! {name} | เมืองหลวง: {capital} | ประชากร: {population} คน | พื้นที่: {area} ตร.กม."

async def run_asyncio_task():
    print("กำลังเริ่มทำงานแบบ Asyncio (ดึงข้อมูลประเทศ Andorra)...")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch_async(session, url)) for url in URLS]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
    duration = time.time() - start_time
    
    for i, res in enumerate(results, 1):
        print(f"รอบที่ {i} -> {res}")
        
    print(f"-> Asyncio ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

def run_asyncio():
    # ป้องกัน Error ในระบบ Windows
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run_asyncio_task())

if __name__ == "__main__":
    run_asyncio()