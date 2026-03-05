import time
import concurrent.futures
import requests

URLS = ["http://olympus.realpython.org/dice"] * 50

def fetch_url(url):
    response = requests.get(url)
    return response.status_code

def run_threading():
    print("กำลังเริ่มทำงานแบบ Threading (I/O Bound)...")
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(fetch_url, URLS)
    duration = time.time() - start_time
    print(f"-> Threading ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

if __name__ == "__main__":
    run_threading()