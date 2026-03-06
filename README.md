# 🐍 ทดลองเขียนโค้ด Thread, Asyncio และ Process Pool ด้วยภาษา Python

**จัดทำโดย:** ชิษณุ แซ่เลี่ยง  
**รหัสนักศึกษา:** 6810110571  
**GitHub Repository:** [psu6810110571/concurrency_hw](https://github.com/psu6810110571/concurrency_hw)  
**วิชา:** TL | **ส่งงาน:** 8 มีนาคม 2026

---

## 📌 โจทย์และเป้าหมาย (Assignment)

งานนี้มีเป้าหมายเพื่อ **ทดลองเขียนโปรแกรมขนาดเล็ก** โดยนำเครื่องมือ Concurrency ของ Python ทั้ง 3 แบบมาใช้จริง ได้แก่

| เครื่องมือ | ประเภทงาน | สิ่งที่โปรแกรมทำ |
|---|---|---|
| **Thread** | I/O Bound | ดึงข้อมูลประเทศจากเว็บแบบ Multi-thread |
| **Asyncio** | I/O Bound | ดึงข้อมูลประเทศจากเว็บแบบ Asynchronous |
| **Process Pool** | CPU Bound | คำนวณผลรวมตัวเลขขนาดใหญ่แบบ Multi-process |

---

## 💡 โปรแกรมที่เขียน (What This Program Does)

โปรแกรมจำลองการดึงข้อมูลประเทศจากเว็บไซต์จริง ([scrapethissite.com](https://www.scrapethissite.com/pages/simple/)) โดย **สุ่มค้นหา** ประเทศ Andorra, Thailand หรือ Japan แล้วแสดงข้อมูล เมืองหลวง, ประชากร และพื้นที่ ควบคู่ไปกับการทดสอบงาน CPU Bound ด้วยการคำนวณผลรวมตัวเลขมหาศาล — ทั้งหมดนี้เพื่อเปรียบเทียบความเร็วและพฤติกรรมของแต่ละวิธี

---

## 📂 โครงสร้างโปรเจกต์ (Project Structure)

```
concurrency_hw/
│
├── main.py              # ไฟล์หลัก รันและเปรียบเทียบผลทั้ง 3 วิธีพร้อมกัน
├── task_thread.py       # I/O Bound ด้วย ThreadPoolExecutor
├── task_asyncio.py      # I/O Bound ด้วย asyncio + aiohttp
├── task_process.py      # CPU Bound ด้วย ProcessPoolExecutor
└── README.md            # เอกสารอธิบายโปรเจกต์ (ไฟล์นี้)
```

---

## 📋 รายละเอียดแต่ละไฟล์ (File Details)

### 1. `task_thread.py` — Threading (I/O Bound)
- ใช้ `ThreadPoolExecutor` เปิด **5 Threads** พร้อมกัน
- แต่ละ Thread ดึง HTML จากเว็บ แล้วใช้ `BeautifulSoup` parse หาข้อมูลประเทศที่สุ่มได้
- เหมาะกับงานที่ต้องรอ Network เพราะ Thread จะสลับกันทำงานระหว่างรอ

### 2. `task_asyncio.py` — Asyncio (I/O Bound)
- ใช้ `aiohttp` + `async/await` ส่ง HTTP request แบบ Non-blocking
- ใช้ `asyncio.gather()` รัน **5 Coroutines** พร้อมกันใน Event Loop เดียว
- Overhead ต่ำกว่า Threading เพราะไม่สร้าง OS Thread จริง

### 3. `task_process.py` — Process Pool (CPU Bound)
- ใช้ `ProcessPoolExecutor` กระจายการคำนวณไปยัง CPU Core แยกกัน
- แต่ละ Process คำนวณ `sum(i*i for i in range(n))` โดย n ≈ 5,000,000
- ก้าวข้ามข้อจำกัดของ **Python GIL** ได้จริง

### 4. `main.py` — Entry Point
- เรียกฟังก์ชันจากทั้ง 3 ไฟล์ต่อเนื่อง เพื่อดูเวลาเปรียบเทียบในคราวเดียว

---

## 🧠 แนวคิดสำคัญ (Key Concepts)

**Python GIL (Global Interpreter Lock)** คือกลไกใน CPython ที่จำกัดให้รัน Python bytecode ได้ทีละ Thread เท่านั้น ทำให้:

- **Threading/Asyncio** → เหมาะกับ I/O Bound (GIL ถูกปล่อยระหว่างรอ I/O)
- **Multiprocessing** → เหมาะกับ CPU Bound (แต่ละ Process มี GIL ของตัวเอง)

| หัวข้อ | Threading | Asyncio | Multiprocessing |
|---|---|---|---|
| **ประเภทงาน** | I/O Bound | I/O Bound | CPU Bound |
| **ติด GIL** | ✅ | ✅ | ❌ |
| **Memory** | แชร์ | แชร์ | แยก |
| **Overhead** | ปานกลาง | ต่ำ | สูง |
| **ความยากในการใช้** | ง่าย | ปานกลาง | ปานกลาง |

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
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

**3. ติดตั้ง Dependencies**
```bash
pip install requests aiohttp beautifulsoup4
```

**4. รันโปรแกรมทั้งหมด**
```bash
python main.py
```

**หรือรันแยกทีละไฟล์**
```bash
python task_thread.py
python task_asyncio.py
python task_process.py
```

---

## 📊 ตัวอย่างผลลัพธ์ (Expected Output)

```
--- เริ่มการทดสอบโปรแกรม Concurrency แบบแยกไฟล์ ---

กำลังเริ่มทำงานแบบ Threading (ดึงข้อมูลประเทศแบบสุ่ม)...
รอบที่ 1 -> สุ่มเจอ! Japan | เมืองหลวง: Tokyo | ประชากร: 127288000 คน | พื้นที่: 377835.0 ตร.กม.
รอบที่ 2 -> สุ่มเจอ! Andorra | เมืองหลวง: Andorra la Vella | ประชากร: 84000 คน | พื้นที่: 468.0 ตร.กม.
รอบที่ 3 -> สุ่มเจอ! Thailand | เมืองหลวง: Bangkok | ประชากร: 67089500 คน | พื้นที่: 514000.0 ตร.กม.
รอบที่ 4 -> สุ่มเจอ! Andorra | เมืองหลวง: Andorra la Vella | ประชากร: 84000 คน | พื้นที่: 468.0 ตร.กม.
รอบที่ 5 -> สุ่มเจอ! Thailand | เมืองหลวง: Bangkok | ประชากร: 67089500 คน | พื้นที่: 514000.0 ตร.กม.
-> Threading ทำงานเสร็จในเวลา: 3.28 วินาที

กำลังเริ่มทำงานแบบ Asyncio (ดึงข้อมูลประเทศแบบสุ่ม)...
รอบที่ 1 -> สุ่มเจอ! Andorra | เมืองหลวง: Andorra la Vella | ประชากร: 84000 คน | พื้นที่: 468.0 ตร.กม.
รอบที่ 2 -> สุ่มเจอ! Japan | เมืองหลวง: Tokyo | ประชากร: 127288000 คน | พื้นที่: 377835.0 ตร.กม.
รอบที่ 3 -> สุ่มเจอ! Thailand | เมืองหลวง: Bangkok | ประชากร: 67089500 คน | พื้นที่: 514000.0 ตร.กม.
รอบที่ 4 -> สุ่มเจอ! Andorra | เมืองหลวง: Andorra la Vella | ประชากร: 84000 คน | พื้นที่: 468.0 ตร.กม.
รอบที่ 5 -> สุ่มเจอ! Andorra | เมืองหลวง: Andorra la Vella | ประชากร: 84000 คน | พื้นที่: 468.0 ตร.กม.
-> Asyncio ทำงานเสร็จในเวลา: 2.21 วินาที

กำลังเริ่มทำงานแบบ Process Pool (CPU Bound)...
รอบที่ 1 -> คำนวณผลรวมเสร็จสิ้น (ตัวเลขยาวมากขอละไว้)
รอบที่ 2 -> คำนวณผลรวมเสร็จสิ้น (ตัวเลขยาวมากขอละไว้)
รอบที่ 3 -> คำนวณผลรวมเสร็จสิ้น (ตัวเลขยาวมากขอละไว้)
รอบที่ 4 -> คำนวณผลรวมเสร็จสิ้น (ตัวเลขยาวมากขอละไว้)
รอบที่ 5 -> คำนวณผลรวมเสร็จสิ้น (ตัวเลขยาวมากขอละไว้)
-> Process Pool ทำงานเสร็จในเวลา: 2.63 วินาที

--- จบการทดสอบ ---
```

> ⚠️ ผลลัพธ์ประเทศจะสุ่มเปลี่ยนในแต่ละรอบ และเวลาขึ้นอยู่กับสเปกเครื่องและความเร็ว Internet

---

## 📦 Dependencies

| ไลบรารี | การใช้งาน | ต้องติดตั้ง |
|---|---|---|
| `requests` | HTTP request แบบ Synchronous | ✅ |
| `aiohttp` | HTTP request แบบ Asynchronous | ✅ |
| `beautifulsoup4` | Parse และดึงข้อมูลจาก HTML | ✅ |
| `concurrent.futures` | ThreadPoolExecutor / ProcessPoolExecutor | ❌ (built-in) |
| `asyncio` | Event Loop และ Coroutine | ❌ (built-in) |

---

## 🔍 สรุปสิ่งที่เรียนรู้ (Summary)

จากผลการทดสอบจริง:

| วิธี | เวลา | หมายเหตุ |
|---|---|---|
| **Threading** | 3.28 วินาที | ช้ากว่าเพราะ Thread switching overhead |
| **Asyncio** | 2.21 วินาที | เร็วที่สุดสำหรับ I/O Bound |
| **Process Pool** | 2.63 วินาที | เหมาะกับ CPU Bound ก้าวข้าม GIL ได้จริง |

**Asyncio เร็วกว่า Threading ประมาณ 33%** สำหรับงาน I/O Bound เนื่องจาก Overhead ต่ำกว่า ในขณะที่ **Process Pool จำเป็นสำหรับงาน CPU Bound** เพราะสามารถใช้ CPU หลาย Core ได้จริง การเลือกใช้เครื่องมือที่เหมาะสมกับประเภทงานจึงมีผลต่อประสิทธิภาพอย่างมีนัยสำคัญ

---

*ชิษณุ แซ่เลี่ยง — 6810110571*