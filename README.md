# Reg Ting Rao

เราจะไม่ทิ้งกันนะ อิอิ

โปรเจคนี้ใช้ Flask และใช้ Virtual Environment ของ Python 
เพื่อให้แยก Dependencies ออกจาก Python ตัวหลักของเครื่องได้

# Installation

## Linux/macOS

- `python --version` -> `3.6.x` ของ Mac น่าจะต้องลง Python 3 ก่อน
- `which pip` -> `pip <someversion> from <somewhere>/python3.x/` ต้องเป็นของ Python 3 นะ
- `pip install pipenv` ถ้าลงไม่ได้ให้ `sudo pip install pipenv`
- เข้าโฟลเดอร์โปรเจค
- `pipenv --three` เพื่อสร้าง Virtual Environment Python 3
- `pipenv shell` เพื่อเข้าสู่ Virtual Environment
- `which python` -> มีคำว่า reg-ting-rao อยู่ในนั้น
- `which pip` -> อยู่ที่เดียวกับ python ข้างบน และมีคำว่า reg-ting-rao อยู่ในผลลัพธ์ของคำสั่ง
- `pipenv install` ถ้าต้องลงอะไรเพิ่มให้ใช้คำสั่ง `pipenv install <packagename>`
- `python reg_ting_rao.py` ควรจะต้องขึ้นว่า `Running on http://0.0.0.0:8080`
- ออกจาก Virtual Environment ด้วยการพิมพ์คำสั่ง `exit` **ไม่ใช่คำสั่ง `deactivate`**

## Windows

- แนะนำให้ใช้ Powershell ดีกว่า ถ้ามี เพราะ Command Prompt แทบไม่มีคำสั่งอะไรให้ใช้เลย - -"
- โหลด Python 3 Version ล่าสุดมาลงก่อน
- ตรงที่ต้องใช้คำสั่ง `sudo` ให้เปิดหน้า Command Prompt/Powershell แบบ Run as Admin
- อย่าลืมเอา Python 3 ใส่ใน PATH ด้วย 
- ตรงที่ต้องใช้คำสั่ง `which <something>` เปลี่ยนเป็น `Get-Command <something>`
- นอกนั้นทำตามข้างบนได้เลย

# References

- [Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Jinja2 Template](http://jinja.pocoo.org/)
- [วิธีลง Python 3 และ Brew Package Manager ใน macOS](http://programwithus.com/learn-to-code/install-python3-mac/)