# 🍪 Cookie Splitter Program

โปรแกรมสำหรับแยกข้อมูลจากไฟล์ `combo.txt` ที่อยู่ในรูปแบบ:


ให้กลายเป็น 2 ไฟล์:
- `user_pass.txt` → เก็บ username:password
- `cookie.txt` → เก็บ cookie อย่างเดียว

---

## 🖥️ วิธีใช้งานโปรแกรม (Windows)

### 1. 📥 ดาวน์โหลดไฟล์
ดาวน์โหลดไฟล์ `cookie_splitter.exe` จาก:
- GitHub Releases
- Google Drive หรือแหล่งที่เจ้าของโปรเจกต์แจก

### 2. 📂 สร้างไฟล์ `combo.txt`
ภายในโฟลเดอร์เดียวกับ `cookie_splitter.exe`  
ให้สร้างไฟล์ `combo.txt` แล้วใส่ข้อมูลในรูปแบบ:

user1:pass1:cookie_data1
user2:pass2:cookie_data2

> สามารถใส่ได้หลายบรรทัด

### 3. ▶️ เปิดโปรแกรม
ดับเบิลคลิก `cookie_splitter.exe`  
หรือคลิกขวา → "Run as administrator" (ถ้าจำเป็น)

### 4. ✅ รอโหลด และผลลัพธ์จะออกมาเป็น:
- `user_pass.txt` → รายชื่อ user:pass ทีละบรรทัด
- `cookie.txt` → รายชื่อ cookie ทีละบรรทัด

หากมีข้อมูลไม่ถูกต้อง โปรแกรมจะแจ้งบรรทัดที่ข้ามไป

---

## 📦 ไฟล์ตัวอย่าง (ในโฟลเดอร์)
- `combo.txt` ← ตัวอย่าง input
- `user_pass.txt` ← output
- `cookie.txt` ← output

---

## 🔒 ความปลอดภัย
- โปรแกรมทำงานออฟไลน์ 100%
- ไม่มีการเชื่อมต่ออินเทอร์เน็ตหรือส่งข้อมูลใด ๆ ออกภายนอก

---

## 🔧 คำแนะนำเพิ่มเติม
- ห้ามใช้ `:` ในชื่อไฟล์อื่น เพราะ Windows ไม่อนุญาต
- ถ้าเปิดแล้วโปรแกรมปิดทันที: ให้เปิดผ่าน `cmd` เพื่อดู error

---

## 👨‍💻 ผู้พัฒนา
- พัฒนาโดย [ชื่อคุณ หรือ GitHub Username]
- โครงการโอเพนซอร์ส: https://github.com/yourname/cookie_splitter
