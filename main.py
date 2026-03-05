# นำเข้าฟังก์ชันจากไฟล์ทั้ง 3 ของเรา
from task_thread import run_threading
from task_asyncio import run_asyncio
from task_process import run_process_pool

if __name__ == "__main__":
    print("--- เริ่มการทดสอบโปรแกรม Concurrency แบบแยกไฟล์ ---\n")
    
    # รันการทดสอบทีละแบบ
    run_threading()
    run_asyncio()
    run_process_pool()
    
    print("--- จบการทดสอบ ---")