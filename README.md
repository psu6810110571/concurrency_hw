# 🐍 การทดลองเขียนโค้ด Thread, Asyncio และ Process Pool ด้วยภาษา Python

**จัดทำโดย:** ชิษณุ แซ่เลี่ยง  
**รหัสนักศึกษา:** 6810110571  
**GitHub Repository:** [psu6810110571/concurrency_hw](https://github.com/psu6810110571/concurrency_hw)

---

## 📖 ภาพรวมของโปรเจกต์ (Project Overview)

โปรเจกต์นี้เปรียบเทียบประสิทธิภาพการทำงานแบบ **Concurrency** ในภาษา Python ด้วย 3 เครื่องมือ ได้แก่ `threading`, `asyncio` และ `Process Pool` เพื่อศึกษาความแตกต่างระหว่างงานประเภท I/O Bound และ CPU Bound

| ประเภทงาน | คำอธิบาย | เครื่องมือที่ใช้ |
|---|---|---|
| **I/O Bound** | งานที่ใช้เวลาส่วนใหญ่รอการรับ-ส่งข้อมูลเครือข่าย | `threading`, `asyncio` |
| **CPU Bound** | งานที่ใช้ทรัพยากร CPU สูงในการประมวลผลคำนวณ | `multiprocessing` (Process Pool) |

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
- ดึงข้อมูล HTML จากเว็บไซต์ [Scrape This Site](https://www.scrapethissite.com/pages/simple/) จำนวน **5 รอบ** พร้อมกัน
- ใช้ `ThreadPoolExecutor` จาก `concurrent.futures` เพื่อสร้าง Thread หลายตัวพร้อมกัน
- ใช้ `BeautifulSoup` ดึงข้อมูลของประเทศ **Andorra** (ชื่อประเทศ, เมืองหลวง, ประชากร, พื้นที่)

### 2. `task_asyncio.py` — I/O Bound ด้วย Asyncio
- ดึงข้อมูลจากเว็บไซต์เดิม **5 รอบ** แบบ Asynchronous
- ใช้ `aiohttp` สำหรับ HTTP request แบบ Non-blocking
- ใช้ `async/await` และ `asyncio.gather()` เพื่อรันหลาย coroutine พร้อมกัน

### 3. `task_process.py` — CPU Bound ด้วย Process Pool
- คำนวณผลรวมของตัวเลขปริมาณมหาศาล **5 ชุด** ด้วย `ProcessPoolExecutor`
- แต่ละ Process รันบน CPU Core แยกกัน ก้าวข้ามข้อจำกัดของ **Python GIL**

### 4. `main.py` — ไฟล์หลัก
- รวบรวมและรันฟังก์ชันจากทั้ง 3 ไฟล์ต่อเนื่องเพื่อเปรียบเทียบเวลาทำงานทั้งหมดในครั้งเดียว

---

## 🧠 แนวคิดสำคัญ (Key Concepts)

**Python GIL (Global Interpreter Lock)** คือกลไกใน CPython ที่อนุญาตให้ Python bytecode ทำงานได้ทีละ Thread เท่านั้น ส่งผลให้ Threading ช่วยได้เฉพาะงาน I/O Bound — หากต้องการใช้ CPU หลายคอร์จริงๆ ต้องใช้ Multiprocessing แทน

| หัวข้อ | Threading | Asyncio | Multiprocessing |
|---|---|---|---|
| **ประเภทงาน** | I/O Bound | I/O Bound | CPU Bound |
| **ติด GIL** | ✅ | ✅ | ❌ |
| **Memory** | แชร์ | แชร์ | แยก |
| **Overhead** | ปานกลาง | ต่ำ | สูง |

---

## ⚙️ การติดตั้งและใช้งาน (Setup & Installation)

**1. โคลนโปรเจกต์**
```bash
git clone https://github.com/psu6810110571/concurrency_hw.git
cd concurrency_hw
```

**2. สร้าง Virtual Environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. ติดตั้ง Dependencies**
```bash
pip install requests aiohttp beautifulsoup4
```

**4. รันโปรแกรม**
```bash
python main.py
```

> รันแยกทีละไฟล์ได้เช่นกัน เช่น `python task_asyncio.py`

---

## 📊 ตัวอย่างผลลัพธ์ (Expected Output)

```
--- เริ่มการทดสอบโปรแกรม Concurrency แบบแยกไฟล์ ---

กำลังเริ่มทำงานแบบ Threading (ดึงข้อมูลประเทศ Andorra)...
รอบที่ 1 -> เจอแล้ว! Andorra | เมืองหลวง: Andorra la Vella | ประชากร: 77281 คน | พื้นที่: 468.0 ตร.กม.
...
-> Threading ทำงานเสร็จในเวลา: 0.85 วินาที

กำลังเริ่มทำงานแบบ Asyncio (ดึงข้อมูลประเทศ Andorra)...
รอบที่ 1 -> เจอแล้ว! Andorra | เมืองหลวง: Andorra la Vella | ประชากร: 77281 คน | พื้นที่: 468.0 ตร.กม.
...
-> Asyncio ทำงานเสร็จในเวลา: 0.52 วินาที

กำลังเริ่มทำงานแบบ Process Pool (CPU Bound)...
รอบที่ 1 -> คำนวณผลรวมเสร็จสิ้น
...
-> Process Pool ทำงานเสร็จในเวลา: 1.20 วินาที

--- จบการทดสอบ ---
```

> เวลาจริงขึ้นอยู่กับสเปกเครื่องและความเร็ว Internet

---

## 📦 Dependencies

| ไลบรารี | การใช้งาน |
|---|---|
| `requests` | HTTP request แบบ Synchronous |
| `aiohttp` | HTTP request แบบ Asynchronous |
| `beautifulsoup4` | Parse และดึงข้อมูลจาก HTML |

> `concurrent.futures` และ `asyncio` เป็น built-in ของ Python ไม่ต้องติดตั้งเพิ่ม

---

*ชิษณุ แซ่เลี่ยง — 6810110571*
