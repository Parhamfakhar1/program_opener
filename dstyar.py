import os
import pyautogui

def open_application(app_name):
    # اینجا می‌توانی نام اپلیکیشن‌هایی که می‌خواهی باز کنی رو اضافه کنی
    apps = {
        'word': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE',
        'excel': 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE',
        'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    }
    
    app_path = apps.get(app_name.lower())
    if app_path:
        os.startfile(app_path)
        print(f"{app_name} opened!")
    else:
        print(f"Application {app_name} not found!")

def main():
    print("Enter a command:")
    while True:
        command = input("Command: ").strip().lower()
        if command == "exit":
            break
        open_application(command)

if __name__ == "__main__":
    main()
