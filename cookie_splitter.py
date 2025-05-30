import os
import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

BANNER = Fore.CYAN + r"""
██████╗ ██╗  ██╗ ██████╗ ████████╗
██╔══██╗██║  ██║██╔═══██╗╚══██╔══╝
██████╔╝███████║██║   ██║   ██║   
██╔═══╝ ██╔══██║██║   ██║   ██║   
██║     ██║  ██║╚██████╔╝   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   
""" + Style.RESET_ALL

def print_banner():
    print(BANNER)

def show_progress_bar(duration=3, length=30):
    print(Fore.YELLOW + "🚀 กำลังโหลดข้อมูล...\n" + Style.RESET_ALL)
    for i in range(length + 1):
        percent = int((i / length) * 100)
        bar = Fore.GREEN + "█" * i + Fore.RED + "-" * (length - i) + Style.RESET_ALL
        sys.stdout.write(f"\r[{bar}] {Fore.CYAN}{percent}%{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(duration / length)
    sys.stdout.write("\n")

def separate_cookies(input_file: str, output_file1: str, output_file2: str):
    if not os.path.exists(input_file):
        print(Fore.YELLOW + f"⚠️ ไม่พบไฟล์ {input_file} กำลังสร้างไฟล์ตัวอย่าง..." + Style.RESET_ALL)
        try:
            with open(input_file, "w", encoding="utf-8") as f:
                f.write("user1:pass1:cookie_data1\nuser2:pass2:cookie_data2\n")
            print(Fore.GREEN + f"✅ สร้าง {input_file} เรียบร้อยแล้ว" + Style.RESET_ALL)
        except Exception as err:
            print(Fore.RED + f"❌ สร้างไฟล์ล้มเหลว: {err}" + Style.RESET_ALL)
        input("กด Enter เพื่อปิดโปรแกรม...")
        return

    show_progress_bar(3)

    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    count_total = 0
    count_success = 0
    count_invalid = 0

    with open(output_file1, "w", encoding="utf-8") as file1, \
         open(output_file2, "w", encoding="utf-8") as file2:
        
        for idx, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue
            count_total += 1

            parts = line.split(":", 2)
            if len(parts) < 3:
                print(Fore.RED + f"[บรรทัด {idx}] ❌ รูปแบบไม่ถูกต้อง: {line}" + Style.RESET_ALL)
                count_invalid += 1
                continue

            user_pass = f"{parts[0]}:{parts[1]}"
            cookie_data = parts[2]

            file1.write(user_pass + "\n")
            file2.write(cookie_data + "\n")
            count_success += 1
    
    print(Fore.GREEN + f"\n✅ แยกข้อมูลเสร็จแล้ว! จากทั้งหมด {count_total} รายการ")
    print(Fore.GREEN + f" - แยกสำเร็จ {count_success} รายการ")
    if count_invalid > 0:
        print(Fore.RED + f" - ข้ามรายการที่ไม่ถูกต้อง {count_invalid} รายการ" + Style.RESET_ALL)
    print(Fore.CYAN + f" - user:pass เก็บที่ => {output_file1}")
    print(Fore.CYAN + f" - cookie data  => {output_file2}" + Style.RESET_ALL)

    input("\nกด Enter เพื่อปิดโปรแกรม...")

if __name__ == '__main__':
    try:
        print_banner()
        input_filename = "combo.txt"
        output_filename1 = "user_pass.txt"
        output_filename2 = "cookie.txt"
        separate_cookies(input_filename, output_filename1, output_filename2)
    except Exception as e:
        print(Fore.RED + f"\n❌ เกิดข้อผิดพลาด: {e}" + Style.RESET_ALL)
        input("กด Enter เพื่อปิดโปรแกรม...")
