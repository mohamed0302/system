@echo off
echo === إنشاء ملف EXE من app.py ===

REM حذف الملفات القديمة
rmdir /s /q build
rmdir /s /q dist
del /q app.spec

REM تنفيذ PyInstaller
pyinstaller --onefile --noconsole app.py

echo === تم الإنشاء! ستجد app.exe داخل مجلد dist ===
pause
