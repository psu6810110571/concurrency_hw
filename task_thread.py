import time
import concurrent.futures
import requests
from bs4 import BeautifulSoup

# ดึงข้อมูล 5 รอบ
URLS = ["https://www.scrapethissite.com/pages/simple/"] * 5

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    countries = soup.find_all('div', class_='country')
    
    for country in countries:
        name = country.find('h3', class_='country-name').text.strip()
        if name == "Andorra":
            capital = country.find('span', class_='country-capital').text.strip()
            population = country.find('span', class_='country-population').text.strip()
            area = country.find('span', class_='country-area').text.strip()
            
            result = f"เจอแล้ว! {name} | เมืองหลวง: {capital} | ประชากร: {population} คน | พื้นที่: {area} ตร.กม."
            return result

def run_threading():
    print("กำลังเริ่มทำงานแบบ Threading (ดึงข้อมูลประเทศ Andorra)...")
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_url, URLS))
        
    duration = time.time() - start_time
    
    for i, res in enumerate(results, 1):
        print(f"รอบที่ {i} -> {res}")
        
    print(f"-> Threading ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

if __name__ == "__main__":
    run_threading()