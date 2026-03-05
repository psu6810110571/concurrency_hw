import time
import concurrent.futures

def calculate(limit):
    return sum(i * i for i in range(limit))

def run_process_pool():
    print("กำลังเริ่มทำงานแบบ Process Pool (CPU Bound)...")
    numbers = [5_000_000 + x for x in range(10)]
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(calculate, numbers)
    duration = time.time() - start_time
    print(f"-> Process Pool ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

if __name__ == "__main__":
    run_process_pool()