# การทดลองเขียนโค้ด Concurrency ใน Python

โปรเจกต์นี้เป็นการทดลองเปรียบเทียบการทำงานของ `threading`, `asyncio` และ `Process Pool` ตามโจทย์ที่ได้รับมอบหมายครับ

## โครงสร้างของโปรแกรม
โปรแกรม (`main.py`) ถูกแบ่งออกเป็น 2 ส่วนหลักเพื่อทดสอบงานที่เหมาะสมกับ Concurrency แต่ละประเภท:

1. **I/O Bound Task (ทดสอบดึงข้อมูลจากเว็บไซต์ 50 ครั้ง)**
   - **Threading:** ใช้ `ThreadPoolExecutor` เพื่อช่วยกันดาวน์โหลดข้อมูล เหมาะกับงานที่ต้องรอเครือข่าย
   - **Asyncio:** ใช้ `aiohttp` และฟีเจอร์ async/await ทำงานสลับกันแบบไม่ต้องรอให้ดาวน์โหลดเสร็จทีละอัน

2. **CPU Bound Task (ทดสอบคำนวณตัวเลขทางคณิตศาสตร์)**
   - **Process Pool:** ใช้ `ProcessPoolExecutor` แยกการคำนวณไปยัง CPU หลายๆ คอร์ เพื่อลดข้อจำกัดของ Python GIL (Global Interpreter Lock)

## วิธีการรันโปรแกรม
1. ติดตั้งไลบรารีที่จำเป็น:
   `pip install requests aiohttp`
2. รันคำสั่ง:
   `python main.py`