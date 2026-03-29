@echo off
chcp 65001 >nul
cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║     🚀 CÔNG CỤ TỰ ĐỘNG TẠO BÁO CÁO PRO VERSION 🚀        ║
echo ║                                                            ║
echo ║  ✨ Tự động sinh nội dung chi tiết                        ║
echo ║  📊 Tự động tạo biểu đồ và sơ đồ                         ║
echo ║  📄 Export Word và PDF                                    ║
echo ║  🤖 Tích hợp AI thông minh                               ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Lỗi: Không tìm thấy Python!
    echo 💡 Vui lòng cài đặt Python từ https://python.org
    pause
    exit /b 1
)

echo 📦 Kiểm tra và cài đặt thư viện...
echo.

pip install -q -r requirements_pro.txt

if errorlevel 1 (
    echo ⚠️  Có lỗi khi cài đặt thư viện
    echo 💡 Thử chạy: pip install --upgrade pip
    pause
    exit /b 1
)

echo ✅ Thư viện đã sẵn sàng!
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo 🎯 CHỌN CHỨC NĂNG:
echo.
echo [1] Tạo báo cáo HOÀN CHỈNH (Word + Biểu đồ)
echo [2] Tạo báo cáo + Export PDF
echo [3] Chỉ tạo biểu đồ test
echo [4] Tùy chỉnh cấu hình
echo [5] Thoát
echo.
set /p choice="Nhập lựa chọn (1-5): "

if "%choice%"=="1" goto full_report
if "%choice%"=="2" goto with_pdf
if "%choice%"=="3" goto diagrams_only
if "%choice%"=="4" goto config
if "%choice%"=="5" goto end

:full_report
echo.
echo 🚀 Đang tạo báo cáo hoàn chỉnh...
python source/auto_report_pro_main.py --mode full
goto done

:with_pdf
echo.
echo 🚀 Đang tạo báo cáo + PDF...
python source/auto_report_pro_main.py --mode pdf
goto done

:diagrams_only
echo.
echo 📊 Đang tạo biểu đồ test...
python source/diagram_generator.py
goto done

:config
echo.
echo ⚙️  Mở file cấu hình...
notepad report_config.json
goto menu

:done
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo ✅ HOÀN THÀNH!
echo.
echo 📁 Các file đã tạo:
echo    - Bao_Cao_Full_Pro.docx (Báo cáo Word)
if "%choice%"=="2" echo    - Bao_Cao_Full_Pro.pdf (Báo cáo PDF)
echo    - diagrams/*.png (Biểu đồ)
echo.
echo 💡 Mở file .docx bằng Microsoft Word để xem
echo.

:end
pause
