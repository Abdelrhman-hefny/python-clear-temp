import os
import time
import shutil

def clear_directory(directory_path):
    """تحذف جميع الملفات والمجلدات داخل مجلد معين مع تجاوز أي عنصر لا يمكن حذفه."""
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
                print(f"تم حذف الملف: {file_path}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"تم حذف المجلد: {file_path}")
        except Exception as e:
            print(f"خطأ أثناء حذف {file_path}: {e}")

def clear_recycle_bin():
    """تحذف جميع الملفات من سلة المهملات في نظام ويندوز."""
    recycle_bin_path = os.path.join(os.environ['SystemDrive'], '$Recycle.Bin')
    for root, dirs, files in os.walk(recycle_bin_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                os.remove(file_path)
                print(f"تم حذف الملف من سلة المهملات: {file_path}")
            except Exception as e:
                print(f"خطأ أثناء حذف {file_path}: {e}")

def clear_unused_files(directory_path, days_unused=30):
    """تحذف الملفات غير المستخدمة منذ عدد محدد من الأيام."""
    current_time = time.time()
    cutoff_time = current_time - (days_unused * 86400)  # 86400 ثانية في اليوم

    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                if os.path.getatime(file_path) < cutoff_time:
                    os.remove(file_path)
                    print(f"تم حذف الملف غير المستخدم: {file_path}")
            except Exception as e:
                print(f"خطأ أثناء حذف {file_path}: {e}")

def clear_adobe_history():
    """تحذف ملفات السجل الخاصة ببرامج أدوبي."""
    adobe_paths = [
        os.path.expandvars(r'%AppData%\Adobe\Logs'),
        os.path.expandvars(r'%LocalAppData%\Adobe\Logs')
    ]
    for path in adobe_paths:
        if os.path.exists(path):
            clear_directory(path)

def main():
    # مسارات الملفات المؤقتة وسلة المهملات
    temp_paths = [
        r"C:\Users\ABDERH~1\AppData\Local\Temp",
        r"C:\Windows\Temp"
    ]

    # تنظيف مجلدات الملفات المؤقتة
    for path in temp_paths:
        print(f"يتم الآن تنظيف: {path}")
        clear_directory(path)

    # تنظيف سلة المهملات
    print("يتم الآن تنظيف سلة المهملات")
    clear_recycle_bin()

    # حذف الملفات غير المستخدمة منذ فترة (مثلاً 30 يوم)
    print("يتم الآن تنظيف الملفات غير المستخدمة منذ فترة")
    clear_unused_files(os.path.expanduser("~"), days_unused=30)

    # حذف ملفات السجل الخاصة ببرامج أدوبي
    print("يتم الآن تنظيف ملفات السجل الخاصة ببرامج أدوبي")
    clear_adobe_history()

if __name__ == "__main__":
    main()
