import time
import concurrent.futures

def calculate(limit):
    # คำนวณผลรวม
    return sum(i * i for i in range(limit))

def run_process_pool():
    print("กำลังเริ่มทำงานแบบ Process Pool (CPU Bound)...")
    # ลดจำนวนรอบลงเหลือ 5 รอบ จะได้ไม่รกจอเกินไป
    numbers = [5_000_000 + x for x in range(5)]
    start_time = time.time()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # 1. เปลี่ยนมาเก็บผลลัพธ์ใส่ list (เหมือนที่เราทำใน Threading)
        results = list(executor.map(calculate, numbers))
        
    duration = time.time() - start_time
    
    # 2. วนลูปปริ้นผลลัพธ์โชว์ทีละรอบ
    for i, res in enumerate(results, 1):
        print(f"รอบที่ {i} -> คำนวณผลรวมเสร็จสิ้น (ตัวเลขยาวมากขอละไว้)")
        
    print(f"-> Process Pool ทำงานเสร็จในเวลา: {duration:.2f} วินาที\n")

if __name__ == "__main__":
    run_process_pool()