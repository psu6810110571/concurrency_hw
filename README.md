# 🐍 การทดลองเขียนโค้ด Thread, Asyncio และ Process Pool ด้วยภาษา Python

**จัดทำโดย:** ชิษณุ แซ่เลี่ยง  
**รหัสนักศึกษา:** 6810110571  
**รายวิชา:** การเขียนโปรแกรมเชิงวัตถุ / Python Programming  
**GitHub Repository:** [psu6810110571/concurrency_hw](https://github.com/psu6810110571/concurrency_hw)

---

## 📖 ภาพรวมของโปรเจกต์ (Project Overview)

โปรเจกต์นี้เป็นการทดลองเปรียบเทียบประสิทธิภาพการทำงานแบบ **Concurrency** ในภาษา Python โดยใช้เครื่องมือ 3 รูปแบบหลัก ได้แก่ `threading`, `asyncio` และ `Process Pool` เพื่อศึกษาความแตกต่างของพฤติกรรมและประสิทธิภาพระหว่างการจัดการงานสองประเภท คือ:

| ประเภทงาน | คำอธิบาย | เครื่องมือที่ใช้ |
|---|---|---|
| **I/O Bound** | งานที่ใช้เวลาส่วนใหญ่รอการรับ-ส่งข้อมูลเครือข่าย | `threading`, `asyncio` |
| **CPU Bound** | งานที่ใช้ทรัพยากร CPU สูงในการประมวลผลคำนวณ | `multiprocessing` (Process Pool) |

---

## 🎯 วัตถุประสงค์ (Objectives)

1. เข้าใจความแตกต่างระหว่าง **Threading**, **Asyncio** และ **Multiprocessing**
2. เปรียบเทียบเวลาการทำงาน (Execution Time) ของแต่ละรูปแบบ
3. เข้าใจข้อจำกัดของ **Python GIL (Global Interpreter Lock)** และวิธีหลีกเลี่ยง
4. ฝึกดึงข้อมูลจากเว็บจริงด้วย `requests`, `aiohttp` และ `BeautifulSoup`

---

## 📂 โครงสร้างโปรเจกต์ (Project Structure)

```
concurrency_hw/
│
├── main.py              # ไฟล์หลัก รันและเปรียบเทียบผลทั้ง 3 วิธีพร้อมกัน
├── task_thread.py       # I/O Bound ด้วย ThreadPoolExecutor
├── task_asyncio.py      # I/O Bound ด้วย asyncio + aiohttp
├── task_process.py      # CPU Bound ด้วย ProcessPoolExecutor
└── README.md            # เอกสารอธิบายโปรเจกต์
```

---

## 📋 รายละเอียดแต่ละไฟล์ (File Details)

### 1. `task_thread.py` — I/O Bound ด้วย Threading

- ดึงข้อมูล HTML จากเว็บไซต์ [Scrape This Site](https://www.scrapethissite.com/pages/simple/) **5 รอบ** พร้อมกัน
- ใช้ `ThreadPoolExecutor` จาก `concurrent.futures` เพื่อสร้าง Thread หลายตัวพร้อมกัน
- ใช้ `BeautifulSoup` เจาะจงดึงข้อมูลของประเทศ **Andorra** (ชื่อประเทศ, เมืองหลวง, ประชากร, พื้นที่)
- **เหมาะกับ:** งานที่ต้องรอ Network I/O และไม่ต้องการประมวลผล CPU หนัก

```python
# ตัวอย่างโครงสร้างหลักของ task_thread.py
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.scrapethissite.com/pages/simple/"

def fetch_andorra(i):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    # ดึงข้อมูล Andorra จาก HTML
    ...

def run_thread():
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(fetch_andorra, range(5))
    print(f"Thread time: {time.time() - start:.2f}s")
```

---

### 2. `task_asyncio.py` — I/O Bound ด้วย Asyncio

- ดึงข้อมูลจากเว็บไซต์เดิม **5 รอบ** แบบ Asynchronous
- ใช้ `aiohttp` สำหรับ HTTP request แบบ Non-blocking
- ใช้ `async/await` และ `asyncio.gather()` เพื่อรันงานหลาย coroutine พร้อมกัน
- **เหมาะกับ:** งาน I/O จำนวนมากที่ต้องการ throughput สูง

```python
# ตัวอย่างโครงสร้างหลักของ task_asyncio.py
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time

URL = "https://www.scrapethissite.com/pages/simple/"

async def fetch_andorra_async(session, i):
    async with session.get(URL) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        # ดึงข้อมูล Andorra จาก HTML
        ...

async def run_asyncio():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch_andorra_async(session, i) for i in range(5)])
    print(f"Asyncio time: {time.time() - start:.2f}s")
```

---

### 3. `task_process.py` — CPU Bound ด้วย Process Pool

- คำนวณผลรวมของตัวเลขปริมาณมหาศาล **5 ชุด** โดยใช้ `ProcessPoolExecutor`
- แต่ละ Process รันบน CPU Core แยกกัน ทำให้ก้าวข้ามข้อจำกัดของ **Python GIL**
- **เหมาะกับ:** งานที่ต้องการพลัง CPU สูง เช่น การประมวลผลภาพ, ML, การคำนวณเชิงวิทยาศาสตร์

```python
# ตัวอย่างโครงสร้างหลักของ task_process.py
from concurrent.futures import ProcessPoolExecutor
import time

def heavy_computation(n):
    return sum(range(n))

def run_process():
    numbers = [10_000_000] * 5
    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_computation, numbers))
    print(f"Process time: {time.time() - start:.2f}s")
    print(f"Results: {results}")
```

---

### 4. `main.py` — ไฟล์หลัก

- รวบรวมและรันฟังก์ชันจากทั้ง 3 ไฟล์ต่อเนื่อง
- แสดงเวลาที่ใช้ของแต่ละวิธีเพื่อเปรียบเทียบผล

---

## 🧠 แนวคิดสำคัญ (Key Concepts)

### Python GIL (Global Interpreter Lock)
GIL คือกลไกใน CPython ที่อนุญาตให้ Python bytecode ทำงานได้ทีละ Thread เท่านั้น ซึ่งส่งผลให้:
- **Threading** ช่วยได้กับงาน I/O Bound (Thread สามารถสลับกันระหว่างรอ I/O)
- **Threading ไม่ช่วย** สำหรับงาน CPU Bound (ต้องใช้ Multiprocessing แทน)

### เปรียบเทียบวิธีการ

| หัวข้อ | Threading | Asyncio | Multiprocessing |
|---|---|---|---|
| **ประเภทงาน** | I/O Bound | I/O Bound | CPU Bound |
| **GIL** | ติดข้อจำกัด | ติดข้อจำกัด | ไม่ติดข้อจำกัด |
| **Memory** | แชร์ Memory | แชร์ Memory | แยก Memory |
| **Overhead** | ปานกลาง | ต่ำ | สูง |
| **ความซับซ้อน** | ง่าย | ปานกลาง | ปานกลาง |

---

## 🌐 แหล่งข้อมูล (Data Source)

- **เว็บไซต์ที่ใช้ Scrape:** [https://www.scrapethissite.com/pages/simple/](https://www.scrapethissite.com/pages/simple/)
- **ข้อมูลที่ดึง:** ข้อมูลประเทศ **Andorra** ได้แก่ ชื่อประเทศ, เมืองหลวง, จำนวนประชากร, และพื้นที่

---

## ⚙️ ขั้นตอนการติดตั้งและใช้งาน (Setup & Installation)

### ความต้องการของระบบ (Requirements)
- Python 3.8 หรือสูงกว่า
- pip (Python Package Manager)
- Git

---

### ขั้นที่ 1: โคลนโปรเจกต์

```bash
git clone https://github.com/psu6810110571/concurrency_hw.git
cd concurrency_hw
```

---

### ขั้นที่ 2: สร้าง Virtual Environment (แนะนำ)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### ขั้นที่ 3: ติดตั้ง Dependencies

```bash
pip install requests aiohttp beautifulsoup4
```

หรือถ้ามีไฟล์ `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### ขั้นที่ 4: รันโปรแกรม

**รันทั้งหมดพร้อมกัน (แนะนำ):**
```bash
python main.py
```

**รันแยกทีละไฟล์:**
```bash
python task_thread.py     # ทดสอบ Threading
python task_asyncio.py    # ทดสอบ Asyncio
python task_process.py    # ทดสอบ Process Pool
```

---

## 📊 ตัวอย่างผลลัพธ์ที่คาดหวัง (Expected Output)

```
===== I/O Bound: Threading =====
[Thread 1] Andorra - Capital: Andorra la Vella | Population: 77,281 | Area: 468.0
[Thread 2] Andorra - Capital: Andorra la Vella | Population: 77,281 | Area: 468.0
...
Threading Time: ~0.8s

===== I/O Bound: Asyncio =====
[Async 1] Andorra - Capital: Andorra la Vella | Population: 77,281 | Area: 468.0
...
Asyncio Time: ~0.5s

===== CPU Bound: Process Pool =====
Result [1]: 49999995000000
Result [2]: 49999995000000
...
Process Pool Time: ~1.2s
```

> **หมายเหตุ:** เวลาจริงขึ้นอยู่กับสเปกเครื่องและความเร็ว Internet

---

## 📦 Dependencies

| ไลบรารี | เวอร์ชัน | การใช้งาน |
|---|---|---|
| `requests` | latest | HTTP request แบบ Synchronous |
| `aiohttp` | latest | HTTP request แบบ Asynchronous |
| `beautifulsoup4` | latest | Parse และดึงข้อมูลจาก HTML |

> ไลบรารี `concurrent.futures`, `asyncio`, และ `multiprocessing` เป็น **built-in** ของ Python ไม่ต้องติดตั้งเพิ่ม

---

## 📚 อ้างอิง (References)

- [Python Official Docs — concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [Python Official Docs — asyncio](https://docs.python.org/3/library/asyncio.html)
- [Python Official Docs — multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [aiohttp Documentation](https://docs.aiohttp.org/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Scrape This Site](https://www.scrapethissite.com/pages/simple/)

---

*README นี้จัดทำขึ้นสำหรับงานทดลองเขียนโค้ด Concurrency ใน Python — ชิษณุ แซ่เลี่ยง (6810110571)*