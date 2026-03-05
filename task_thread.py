import time
import concurrent.futures
import requests

# เปลี่ยนเป็นเว็บเป้าหมาย และลดเหลือ 10 รอบ
URLS = ["https://www.scrapethissite.com/pages/simple/"] * 10

def fetch_url(url):
    response = requests.get(url)
    html_content = response.text  # ดึงเนื้อหา HTML ของหน้าเว็บมาเก็บไว้
    return len(html_content)      # คืนค่าเป็น 'จำนวนตัวอักษร' เพื่อให้หน้าจอไม่รก

def run_threading():
    print("กำลังเริ่มทำงานแบบ Threading (ดึงข้อมูลเว็บจริง)...")
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # เก็บผลลัพธ์ที่ดึงมาได้
        results = list(executor.map(fetch_url, URLS))
    duration = time.time() - start_time
    
    # ปริ้นโชว์ว่าดึงมาได้กี่ตัวอักษร
    print(f"-> โหลดข้อมูลขนาด {results[0]} ตัวอักษร จำนวน {len(URLS)} หน้า")
    print(f"-> Threading ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

if __name__ == "__main__":
    run_threading()